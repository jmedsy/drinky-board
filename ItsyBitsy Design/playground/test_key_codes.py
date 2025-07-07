#!/usr/bin/env python3

from pynput import keyboard

def on_press(key):
    print(f"Pressed: {str(key)}")
    print(f"Type: {type(key)}")
    print(f"Dir: {[attr for attr in dir(key) if not attr.startswith('_')]}")
    if hasattr(key, 'location'):
        print(f"Location: {key.location}")
    else:
        print("Location: N/A")
    if hasattr(key, 'char'):
        print(f"Char: {key.char}")
    if hasattr(key, 'vk'):
        print(f"VK: {key.vk}")
    print("---")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False

print("Press keys to see their string representations (ESC to exit):")
print("Try pressing: forward slash (/), space, enter, a, 1, etc.")
print("=" * 50)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 