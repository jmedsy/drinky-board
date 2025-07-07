#region Imports
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pynput import keyboard
from collections import deque
import asyncio
from time import sleep
import struct
import serial
import glob
from backend.logic.keymaps.key_definitions import KEYS
from backend.logic.keygroup.keygroup import KeyGroup, get_keymap_name
#endregio

#region Global Variables
key_queue = deque()
ser = None  # Global variable for serial connection
pressed_modifiers = set()
eligible_modifiers = {keyboard.Key.shift, keyboard.Key.shift_r, keyboard.Key.cmd, keyboard.Key.alt, keyboard.Key.ctrl, keyboard.Key.esc}
#endregion

#region Helper Functions
def find_itsybitsy_port():
    """Find the ItsyBitsy port by searching for USB ports"""
    ports = glob.glob('/dev/tty.usbmodem*')
    if not ports:
        raise Exception("No ItsyBitsy found. Please connect the device.")
    return ports[0]

def send_command(ser, key, action):
    """Send a command to the Arduino"""
    command = struct.pack('>BBBBBBBBBBBBB',
        key.row.i2c_addr,
        key.row.logi_pin,
        key.row.pin.axis.value,
        key.row.pin.channel,
        key.row.bus_pin.axis.value,
        key.row.bus_pin.channel,
        key.col.i2c_addr,
        key.col.logi_pin,
        key.col.pin.axis.value,
        key.col.pin.channel,
        key.col.bus_pin.axis.value,
        key.col.bus_pin.channel,
        1 if action == "PRESS" else 0
    )
    ser.write(command)
    ser.flush()

def on_press(key):
    global ser

    # Exit program on Esc key
    if key == keyboard.Key.esc:
        return False

    # Track modifier key
    if key in eligible_modifiers:
        pressed_modifiers.add(key)

    # Add key to queue
    key_queue.append(key)

    # Process queue
    while len(key_queue) > 0:
        current_key = key_queue.popleft()
        if current_key == keyboard.Key.esc:
            break

        # Skip modifier key (as its handled independently)
        if current_key in eligible_modifiers:
            continue

        # print(key)

        # Create keygroup using tracked modifiers and base key
        my_keygroup = KeyGroup(base=str(get_keymap_name(current_key, 'bash')), modifiers=frozenset(pressed_modifiers))

        # Press modifier key(s)
        for mk in my_keygroup.modifiers:
            keymap_name = get_keymap_name(mk, 'bash')
            if keymap_name is not None:
                modifier_key = getattr(KEYS, get_keymap_name(mk, 'bash'))
                if modifier_key:
                    send_command(ser, modifier_key, 'PRESS')

        if my_keygroup.base is not None:
            mapped_key = getattr(KEYS, my_keygroup.base)
            if mapped_key is not None:
                send_command(ser, mapped_key, 'PRESS')
                sleep(0.02)
                send_command(ser, mapped_key, 'RELEASE')
                sleep(0.02)

        # Release modifier key(s)
        for mk in my_keygroup.modifiers:
            keymap_name = get_keymap_name(mk, 'bash')
            if keymap_name is not None:
                modifier_key = getattr(KEYS, get_keymap_name(mk, 'bash'))
                if modifier_key:
                    send_command(ser, modifier_key, 'RELEASE')

def on_release(key):
    if key in eligible_modifiers:
        pressed_modifiers.remove(key)
#endregion

#region Main
def main():
    global ser
    # Find and open serial port
    port = find_itsybitsy_port()
    print(f"Found ItsyBitsy at {port}")
    
    # Open serial port
    ser = serial.Serial(port, 115200, timeout=0.001)
    print("Serial port opened successfully")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # Cleanup
    ser.close()

if __name__ == "__main__":
    main() 
#endregion