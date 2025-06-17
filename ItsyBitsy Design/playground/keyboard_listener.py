#!/usr/bin/env python3

from pynput import keyboard

def on_press(key):
    try:
        # For regular character keys
        print(f'Key pressed: {key.char}', end='', flush=True)
    except AttributeError:
        # For special keys like space, enter, etc.
        if key == keyboard.Key.space:
            print(' ', end='', flush=True)
        elif key == keyboard.Key.enter:
            print('\n', end='', flush=True)
        elif key == keyboard.Key.backspace:
            print('\b \b', end='', flush=True)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on ESC key
        print("\nExiting...")
        return False

def main():
    print("Type something (press ESC to exit):")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main() 