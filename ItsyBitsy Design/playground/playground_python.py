import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import serial
import struct
import time
import glob
from pynput import keyboard
from backend.logic.keymaps.key_definitions import KEYS

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

def main():
    # Find and open serial port
    port = find_itsybitsy_port()
    print(f"Found ItsyBitsy at {port}")
    
    # Open serial port
    ser = serial.Serial(port, 115200, timeout=0.001)
    print("Serial port opened successfully")
    
    # Track key states
    key_states = {}
    
    def on_press(key):
        try:
            # Handle special keys
            if hasattr(key, 'char') and key.char:
                if key.char in key_states and key_states[key.char]:
                    return  # Key already pressed
                key_states[key.char] = True
                key_mapping = getattr(KEYS, key.char.upper(), None)
                if key_mapping:
                    send_command(ser, key_mapping, "PRESS")
            elif key in SPECIAL_KEY_MAP:
                if key in key_states and key_states[key]:
                    return  # Key already pressed
                key_states[key] = True
                send_command(ser, SPECIAL_KEY_MAP[key], "PRESS")
        except Exception as e:
            print(f"Error in on_press: {e}")
    
    def on_release(key):
        try:
            # Handle special keys
            if hasattr(key, 'char') and key.char:
                if not key_states.get(key.char, False):
                    return  # Key wasn't pressed
                key_states[key.char] = False
                key_mapping = getattr(KEYS, key.char.upper(), None)
                if key_mapping:
                    send_command(ser, key_mapping, "RELEASE")
            elif key in SPECIAL_KEY_MAP:
                if not key_states.get(key, False):
                    return  # Key wasn't pressed
                key_states[key] = False
                send_command(ser, SPECIAL_KEY_MAP[key], "RELEASE")
            
            # Stop listener on escape
            if key == keyboard.Key.esc:
                return False
        except Exception as e:
            print(f"Error in on_release: {e}")
    
    # Special key mappings
    SPECIAL_KEY_MAP = {
        keyboard.Key.space: KEYS.SPACE,
        keyboard.Key.backspace: KEYS.BACKSPACE
    }
    
    # Start keyboard listener
    print("Ready! Press any alphanumeric key (A-Z, 0-9), space, or backspace to send command. Press Escape to exit.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    # Cleanup
    ser.close()

if __name__ == "__main__":
    main() 