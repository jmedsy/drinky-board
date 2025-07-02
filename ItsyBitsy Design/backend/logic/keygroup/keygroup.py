from dataclasses import dataclass
from typing import FrozenSet
from pynput import keyboard

@dataclass(frozen=True)
class KeyGroup:
    base: str
    modifiers: FrozenSet[str]

# Helper for finding the keymap from different environments
def get_keymap_name(key, env:str) -> str:
    match env:
        case 'bash':
            if key == keyboard.Key.shift or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                return 'LEFT_SHIFT'
            elif key == keyboard.Key.cmd:
                return 'LEFT_CTRL'
            elif key == keyboard.Key.alt:
                return 'LEFT_ALT'
            elif key == keyboard.Key.ctrl:
                return 'LEFT_WINDOWS'
            elif key == keyboard.Key.space:
                return 'SPACE'
            elif key == keyboard.Key.backspace:
                return 'BACKSPACE'
            elif key == keyboard.Key.enter:
                return 'ENTER'
            elif key == keyboard.Key.caps_lock:
                return 'CAPS_LOCK'
            elif key == keyboard.Key.tab:
                return 'TAB'
            elif key == keyboard.Key.esc:
                return 'ESCAPE'
            elif key == keyboard.Key.up:
                return 'UP'
            elif key == keyboard.Key.down:
                return 'DOWN'
            elif key == keyboard.Key.left:
                return 'LEFT'
            elif key == keyboard.Key.right:
                return 'RIGHT'
            elif key == keyboard.Key.f1:
                return 'F1'
            elif key == keyboard.Key.f2:
                return 'F2'
            elif key == keyboard.Key.f3:
                return 'F3'
            elif key == keyboard.Key.f4:
                return 'F4'
            elif key == keyboard.Key.f5:
                return 'F5'
            elif key == keyboard.Key.f6:
                return 'F6'
            elif key == keyboard.Key.f7:
                return 'F7'
            elif key == keyboard.Key.f8:
                return 'F8'
            elif key == keyboard.Key.f9:
                return 'F9'
            elif key == keyboard.Key.f10:
                return 'F10'
            elif key == keyboard.Key.f11:
                return 'F11'
            elif key == keyboard.Key.f12:
                return 'F12'
            elif key == keyboard.Key.delete:
                return 'DELETE'
            # elif key == keyboard.Key.insert:
            #     return 'INSERT'
            elif key == keyboard.Key.home:
                return 'HOME'
            elif key == keyboard.Key.end:
                return 'END'
            elif key == keyboard.Key.page_up:
                return 'PAGE_UP'
            elif key == keyboard.Key.page_down:
                return 'PAGE_DOWN'
            elif type(key) is str and key.startswith('Key.'):
                return key[4:].upper()
            elif hasattr(key, 'char'):
                if key.char == '1' or key.char == '!':
                    return 'NUM_1'
                if key.char == '2' or key.char == '@':
                    return 'NUM_2'
                if key.char == '3' or key.char == '#':
                    return 'NUM_3'
                if key.char == '4' or key.char == '$':
                    return 'NUM_4'
                if key.char == '5' or key.char == '%':
                    return 'NUM_5'
                if key.char == '6' or key.char == '^':
                    return 'NUM_6'
                if key.char == '7' or key.char == '&':
                    return 'NUM_7'
                if key.char == '8' or key.char == '*':
                    return 'NUM_8'
                if key.char == '9' or key.char == '(':
                    return 'NUM_9'
                if key.char == '0' or key.char == ')':
                    return 'NUM_0'
                if key.char == '-' or key.char == '_':
                    return 'MINUS'
                if key.char == '=' or key.char == '+':
                    return 'EQUALS'
                if key.char == '.' or key.char == '>':
                    return 'PERIOD'
                if key.char == ',' or key.char == '<':
                    return 'COMMA'
                if key.char == '/' or key.char == '?':
                    return 'FORWARD_SLASH'
                if key.char == ';' or key.char == ':':
                    return 'SEMICOLON'
                if key.char == "'" or key.char == '"':
                    return 'APOSTROPHE'
                if key.char == '[' or key.char == '{':
                    return 'OPENING_BRACKET'
                if key.char == ']' or key.char == '}':
                    return 'CLOSING_BRACKET'
                if key.char == '\\' or key.char == '|':
                    return 'BACKSLASH'
                if key.char == '`':
                    return 'BACKTICK'
                if key.char == '\x05':
                    return 'INSERT'
                if key.char == '\x03':
                    return 'ENTER'
                else:
                    return key.char.capitalize()
            else:
                return None