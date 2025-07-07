'''
Key Definitions for the Drinky Board

This file contains the complete key definitions for the Drinky Board keyboard controller.
Each key definition includes both physical mapping information (for hardware control)
and string aliases (for client-side identification).

Structure:
- KEYS: A class containing all key definitions as class attributes
- Each key is a KeyDefinition object with:
  - physical_mapping: Hardware pin assignments (row/col, I2C addresses, etc.)
  - string_aliases: Client-specific string identifiers (e.g., web_client uses JavaScript key codes)

Usage:
- Import KEYS to access key definitions: from logic.keymaps.key_definitions import KEYS
- Access individual keys: KEYS.A, KEYS.SPACE, KEYS.LEFT_CTRL, etc.
- Use for hardware control: itsy_device.send_command(KEYS.A, 'PRESS')
- Use for client mapping: Check key.string_aliases.web_client for JavaScript key codes

This is the central source of truth for all key mappings in the Drinky Board system.
'''

from dataclasses import dataclass
from typing import Set
from .adg2128_axis import Axis
from .adg2128_pin import ADG2128Pin, get_bus_pin

ROW_I2C_ADDR = 0x70
COL_I2C_ADDR = 0x71

@dataclass(frozen=True)
class Pin:
    i2c_addr: int
    logi_pin: int
    pin: ADG2128Pin
    bus_pin: ADG2128Pin = None

    # If no bus pin is explicitly provided, get_bus_pin() automaticaly sets it (recommended)
    def __post_init__(self):
        if self.bus_pin is None:
            object.__setattr__(self, 'bus_pin', get_bus_pin(self.pin))

@dataclass(frozen=True)
class PhysicalMapping:
    row: Pin
    col: Pin

@dataclass(frozen=True)
class StringAliases:
    web_client: Set[str]

@dataclass(frozen=True)
class KeyDefinition:
    physical_mapping: PhysicalMapping
    string_aliases: StringAliases

class KEYS:
    ESCAPE = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
        ),
        string_aliases=StringAliases(
            web_client={'Escape'}
        )
    )
    F8 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
        ),
        string_aliases=StringAliases(
            web_client={'F8'}
        )
    )
    PRINT_SCREEN = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
        ),
        string_aliases=StringAliases(
            web_client={'PrintScreen'}
        )
    )
    F10 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
        ),
        string_aliases=StringAliases(
            web_client={'F10'}
        )
    )
    F6 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
        ),
        string_aliases=StringAliases(
            web_client={'F6'}
        )
    )
    F4 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
        ),
        string_aliases=StringAliases(
            web_client={'F4'}
        )
    )
    F5 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
        ),
        string_aliases=StringAliases(
            web_client={'F5'}
        )
    )
    NUMPAD_FORWARD_SLASH = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
        ),
        string_aliases=StringAliases(
            web_client={'NumpadDivide'}
        )
    )
    CLOSING_BRACKET = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
        ),
        string_aliases=StringAliases(
            web_client={'BracketRight'}
        )
    )
    NUMPAD_4 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
        ),
        string_aliases=StringAliases(
            web_client={'Numpad4'}
        )
    )
    F2 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
        ),
        string_aliases=StringAliases(
            web_client={'F2'}
        )
    )
    F1 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
        ),
        string_aliases=StringAliases(
            web_client={'F1'}
        )
    )
    LEFT_ALT = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=25, pin=ADG2128Pin(Axis.X, 8))
        ),
        string_aliases=StringAliases(
            web_client={'AltLeft'}
        )
    )
    BACKTICK = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
        ),
        string_aliases=StringAliases(
            web_client={'Backquote'}
        )
    )
    F9 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
        ),
        string_aliases=StringAliases(
            web_client={'F9'}
        )
    )
    SCROLL_LOCK = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
        ),
        string_aliases=StringAliases(
            web_client={'ScrollLock'}
        )
    )
    F11 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
        ),
        string_aliases=StringAliases(
            web_client={'F11'}
        )
    )
    F7 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
        ),
        string_aliases=StringAliases(
            web_client={'F7'}
        )
    )
    NUM_4 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
        ),
        string_aliases=StringAliases(
            web_client={'Digit4'}
        )
    )
    T = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
        ),
        string_aliases=StringAliases(
            web_client={'KeyT'}
        )
    )
    NUMPAD_8 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
        ),
        string_aliases=StringAliases(
            web_client={'Numpad8'}
        )
    )
    LEFT_WINDOWS = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=11, pin=ADG2128Pin(Axis.Y, 4))
        ),
        string_aliases=StringAliases(
            web_client={'MetaLeft'}
        )
    )
    BACKSPACE = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
        ),
        string_aliases=StringAliases(
            web_client={'Backspace'}
        )
    )
    BACKSLASH = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
        ),
        string_aliases=StringAliases(
            web_client={'Backslash'}
        )
    )
    NUMPAD_1 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
        ),
        string_aliases=StringAliases(
            web_client={'Numpad1'}
        )
    )
    F3 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
        ),
        string_aliases=StringAliases(
            web_client={'F3'}
        )
    )
    NUM_1 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
        ),
        string_aliases=StringAliases(
            web_client={'Digit1'}
        )
    )
    LEFT_CTRL = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=1, pin=ADG2128Pin(Axis.X, 0))
        ),
        string_aliases=StringAliases(
            web_client={'ControlLeft'}
        )
    )
    TAB = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
        ),
        string_aliases=StringAliases(
            web_client={'Tab'}
        )
    )
    NUM_8 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
        ),
        string_aliases=StringAliases(
            web_client={'Digit8'}
        )
    )
    PAUSE_BREAK = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
        ),
        string_aliases=StringAliases(
            web_client={'Pause'}
        )
    )
    F12 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
        ),
        string_aliases=StringAliases(
            web_client={'F12'}
        )
    )
    U = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
        ),
        string_aliases=StringAliases(
            web_client={'KeyU'}
        )
    )
    R = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
        ),
        string_aliases=StringAliases(
            web_client={'KeyR'}
        )
    )
    NUM_6 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
        ),
        string_aliases=StringAliases(
            web_client={'Digit6'}
        )
    )
    END = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
        ),
        string_aliases=StringAliases(
            web_client={'End'}
        )
    )
    P = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
        ),
        string_aliases=StringAliases(
            web_client={'KeyP'}
        )
    )
    DELETE = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
        ),
        string_aliases=StringAliases(
            web_client={'Delete'}
        )
    )
    NUMPAD_2 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
        ),
        string_aliases=StringAliases(
            web_client={'Numpad2'}
        )
    )
    NUM_3 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
        ),
        string_aliases=StringAliases(
            web_client={'Digit3'}
        )
    )
    NUM_2 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
        ),
        string_aliases=StringAliases(
            web_client={'Digit2'}
        )
    )
    Q = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
        ),
        string_aliases=StringAliases(
            web_client={'KeyQ'}
        )
    )
    NUM_9 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
        ),
        string_aliases=StringAliases(
            web_client={'Digit9'}
        )
    )
    PAGE_UP = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
        ),
        string_aliases=StringAliases(
            web_client={'PageUp'}
        )
    )
    MINUS = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
        ),
        string_aliases=StringAliases(
            web_client={'Minus'}
        )
    )
    H = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
        ),
        string_aliases=StringAliases(
            web_client={'KeyH'}
        )
    )
    NUM_5 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
        ),
        string_aliases=StringAliases(
            web_client={'Digit5'}
        )
    )
    ENTER = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
        ),
        string_aliases=StringAliases(
            web_client={'Enter'}
        )
    )
    Y = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
        ),
        string_aliases=StringAliases(
            web_client={'KeyY'}
        )
    )
    LEFT_SHIFT = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=9, pin=ADG2128Pin(Axis.Y, 2))
        ),
        string_aliases=StringAliases(
            web_client={'ShiftLeft'}
        )
    )
    NUMPAD_ASTERISK = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
        ),
        string_aliases=StringAliases(
            web_client={'NumpadMultiply'}
        )
    )
    OPENING_BRACKET = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
        ),
        string_aliases=StringAliases(
            web_client={'BracketLeft'}
        )
    )
    NUMPAD_3 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
        ),
        string_aliases=StringAliases(
            web_client={'Numpad3'}
        )
    )
    E = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
        ),
        string_aliases=StringAliases(
            web_client={'KeyE'}
        )
    )
    W = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
        ),
        string_aliases=StringAliases(
            web_client={'KeyW'}
        )
    )
    RIGHT_CTRL = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=1, pin=ADG2128Pin(Axis.X, 0))
        ),
        string_aliases=StringAliases(
            web_client={'ControlRight'}
        )
    )
    A = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
        ),
        string_aliases=StringAliases(
            web_client={'KeyA'}
        )
    )
    NUM_0 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
        ),
        string_aliases=StringAliases(
            web_client={'Digit0'}
        )
    )
    NUM_LOCK = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
        ),
        string_aliases=StringAliases(
            web_client={'NumLock'}
        )
    )
    EQUALS = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
        ),
        string_aliases=StringAliases(
            web_client={'Equal'}
        )
    )
    NUM_7 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
        ),
        string_aliases=StringAliases(
            web_client={'Digit7'}
        )
    )
    F = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
        ),
        string_aliases=StringAliases(
            web_client={'KeyF'}
        )
    )
    G = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
        ),
        string_aliases=StringAliases(
            web_client={'KeyG'}
        )
    )
    NUMPAD_7 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
        ),
        string_aliases=StringAliases(
            web_client={'Numpad7'}
        )
    )
    SEMICOLON = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
        ),
        string_aliases=StringAliases(
            web_client={'Semicolon'}
        )
    )
    UP = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
        ),
        string_aliases=StringAliases(
            web_client={'ArrowUp'}
        )
    )
    NUMPAD_MINUS = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
        ),
        string_aliases=StringAliases(
            web_client={'NumpadSubtract'}
        )
    )
    D = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
        ),
        string_aliases=StringAliases(
            web_client={'KeyD'}
        )
    )
    O = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
        ),
        string_aliases=StringAliases(
            web_client={'KeyO'}
        )
    )
    HOME = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
        ),
        string_aliases=StringAliases(
            web_client={'Home'}
        )
    )
    I = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
        ),
        string_aliases=StringAliases(
            web_client={'KeyI'}
        )
    )
    J = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
        ),
        string_aliases=StringAliases(
            web_client={'KeyJ'}
        )
    )
    V = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
        ),
        string_aliases=StringAliases(
            web_client={'KeyV'}
        )
    )
    B = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
        ),
        string_aliases=StringAliases(
            web_client={'KeyB'}
        )
    )
    NUMPAD_9 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
        ),
        string_aliases=StringAliases(
            web_client={'Numpad9'}
        )
    )
    APOSTROPHE = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
        ),
        string_aliases=StringAliases(
            web_client={'Quote'}
        )
    )
    RIGHT = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
        ),
        string_aliases=StringAliases(
            web_client={'ArrowRight'}
        )
    )
    NUMPAD_PLUS = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
        ),
        string_aliases=StringAliases(
            web_client={'NumpadAdd'}
        )
    )
    C = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
        ),
        string_aliases=StringAliases(
            web_client={'KeyC'}
        )
    )
    X = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
        ),
        string_aliases=StringAliases(
            web_client={'KeyX'}
        )
    )
    RIGHT_ALT = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=25, pin=ADG2128Pin(Axis.X, 8))
        ),
        string_aliases=StringAliases(
            web_client={'AltRight'}
        )
    )
    Z = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
        ),
        string_aliases=StringAliases(
            web_client={'KeyZ'}
        )
    )
    L = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
        ),
        string_aliases=StringAliases(
            web_client={'KeyL'}
        )
    )
    PAGE_DOWN = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
        ),
        string_aliases=StringAliases(
            web_client={'PageDown'}
        )
    )
    LEFT = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
        ),
        string_aliases=StringAliases(
            web_client={'ArrowLeft'}
        )
    )
    N = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
        ),
        string_aliases=StringAliases(
            web_client={'KeyN'}
        )
    )
    M = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
        ),
        string_aliases=StringAliases(
            web_client={'KeyM'}
        )
    )
    COMMA = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
        ),
        string_aliases=StringAliases(
            web_client={'Comma'}
        )
    )
    NUMPAD_5 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
        ),
        string_aliases=StringAliases(
            web_client={'Numpad5'}
        )
    )
    K = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
        ),
        string_aliases=StringAliases(
            web_client={'KeyK'}
        )
    )
    NUMPAD_0 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
        ),
        string_aliases=StringAliases(
            web_client={'Numpad0'}
        )
    )
    S = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
        ),
        string_aliases=StringAliases(
            web_client={'KeyS'}
        )
    )
    RIGHT_WINDOWS = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=26, pin=ADG2128Pin(Axis.X, 7))
        ),
        string_aliases=StringAliases(
            web_client={'MetaRight'}
        )
    )
    CAPS_LOCK = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
        ),
        string_aliases=StringAliases(
            web_client={'CapsLock'}
        )
    )
    FORWARD_SLASH = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
        ),
        string_aliases=StringAliases(
            web_client={'Slash'}
        )
    )
    INSERT = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
        ),
        string_aliases=StringAliases(
            web_client={'Insert'}
        )
    )
    RIGHT_SHIFT = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
        ),
        string_aliases=StringAliases(
            web_client={'ShiftRight'}
        )
    )
    PERIOD = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
        ),
        string_aliases=StringAliases(
            web_client={'Period'}
        )
    )
    RIGHT_FUNCTION = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
        ),
        string_aliases=StringAliases(
            web_client={'foo'}
        )
    )
    NUMPAD_6 = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
        ),
        string_aliases=StringAliases(
            web_client={'Numpad6'}
        )
    )
    DOWN = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
        ),
        string_aliases=StringAliases(
            web_client={'ArrowDown'}
        )
    )
    SPACE = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
        ),
        string_aliases=StringAliases(
            web_client={'Space'}
        )
    )
    NUMPAD_ENTER = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
        ),
        string_aliases=StringAliases(
            web_client={'NumpadEnter'}
        )
    )
    NUMPAD_PERIOD = KeyDefinition(
        physical_mapping=PhysicalMapping(
            row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
            col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
        ),
        string_aliases=StringAliases(
            web_client={'NumpadDecimal'}
        )
    )