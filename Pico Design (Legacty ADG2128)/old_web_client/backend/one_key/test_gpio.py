from pyftdi.gpio import GpioController
from pynput import keyboard
import time

gpio = GpioController()
gpio.configure('ftdi://ftdi:232h:1/1', direction=0x01)
gpio.write(0x00)
print(f"GPIO initialized: {gpio.read():08b} (D0 LOW)")

# Track whether space is held
is_space_held = False

def on_press(key):
    global is_space_held
    if key == keyboard.Key.space:
        is_space_held = True
        gpio.write(0x01)

def on_release(key):
    global is_space_held
    if key == keyboard.Key.space:
        is_space_held = False
        gpio.write(0x00)

# Set up the listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

print("Hold SPACE to trigger key. Press Ctrl+C to exit.")

try:
    while True:
        time.sleep(0.1)  # Keep main thread alive
except KeyboardInterrupt:
    print("\nExiting. Releasing key and cleaning up.")
    gpio.write(0x00)
    gpio.close()
    listener.stop()
