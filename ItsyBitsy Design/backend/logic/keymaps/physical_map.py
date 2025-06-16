from dataclasses import dataclass
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
class Mapping:
    row: Pin
    col: Pin

class KEYS:
    ESCAPE = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
    )
    F8 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
    )
    PRINT_SCREEN = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
    )
    F10 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
    )
    F6 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
    )
    F4 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
    )
    F5 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
    )
    NUMPAD_FORWARD_SLASH = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
    )
    CLOSING_BRACKET = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
    )
    NUMPAD_4 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
    )
    F2 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
    )
    F1 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
    )
    LEFT_ALT = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=14, pin=ADG2128Pin(Axis.Y, 5)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=25, pin=ADG2128Pin(Axis.X, 8))
    )
    BACKTICK = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
    )
    F9 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
    )
    SCROLL_LOCK = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
    )
    F11 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
    )
    F7 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
    )
    NUM_4 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
    )
    T = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
    )
    NUMPAD_8 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
    )
    LEFT_WINDOWS = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=11, pin=ADG2128Pin(Axis.Y, 4))
    )
    BACKSPACE = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
    )
    BACKSLASH = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
    )
    NUMPAD_1 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
    )
    F3 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
    )
    NUM_1 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=15, pin=ADG2128Pin(Axis.Y, 6)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
    )
    LEFT_CTRL = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=1, pin=ADG2128Pin(Axis.X, 0))
    )
    TAB = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
    )
    NUM_8 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
    )
    PAUSE_BREAK = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
    )
    F12 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
    )
    U = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
    )
    R = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
    )
    NUM_6 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
    )
    END = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
    )
    P = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
    )
    DELETE = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
    )
    NUMPAD_2 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
    )
    NUM_3 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
    )
    NUM_2 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=16, pin=ADG2128Pin(Axis.X, 11)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
    )
    Q = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
    )
    NUM_9 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
    )
    PAGE_UP = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
    )
    MINUS = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
    )
    H = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
    )
    NUM_5 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
    )
    ENTER = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
    )
    Y = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
    )
    LEFT_SHIFT = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=9, pin=ADG2128Pin(Axis.Y, 2))
    )
    NUMPAD_ASTERISK = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
    )
    OPENING_BRACKET = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
    )
    NUMPAD_3 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
    )
    E = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
    )
    W = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=17, pin=ADG2128Pin(Axis.X, 10)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
    )
    RIGHT_CTRL = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=1, pin=ADG2128Pin(Axis.X, 0))
    )
    A = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
    )
    NUM_0 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
    )
    NUM_LOCK = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
    )
    EQUALS = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
    )
    NUM_7 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
    )
    F = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
    )
    G = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
    )
    NUMPAD_7 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
    )
    SEMICOLON = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
    )
    UP = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
    )
    NUMPAD_MINUS = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
    )
    D = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=18, pin=ADG2128Pin(Axis.X, 9)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
    )
    O = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
    )
    HOME = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
    )
    I = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
    )
    J = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
    )
    V = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
    )
    B = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
    )
    NUMPAD_9 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
    )
    APOSTROPHE = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
    )
    RIGHT = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
    )
    NUMPAD_PLUS = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
    )
    C = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=23, pin=ADG2128Pin(Axis.X, 10))
    )
    X = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
    )
    RIGHT_ALT = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=19, pin=ADG2128Pin(Axis.X, 8)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=25, pin=ADG2128Pin(Axis.X, 8))
    )
    Z = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
    )
    L = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
    )
    PAGE_DOWN = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
    )
    LEFT = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
    )
    N = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
    )
    M = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
    )
    COMMA = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=8, pin=ADG2128Pin(Axis.Y, 1))
    )
    NUMPAD_5 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
    )
    K = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
    )
    NUMPAD_0 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
    )
    S = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
    )
    RIGHT_WINDOWS = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=20, pin=ADG2128Pin(Axis.X, 7)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=26, pin=ADG2128Pin(Axis.X, 7))
    )
    CAPS_LOCK = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=2, pin=ADG2128Pin(Axis.X, 1))
    )
    FORWARD_SLASH = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=3, pin=ADG2128Pin(Axis.X, 2))
    )
    INSERT = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=4, pin=ADG2128Pin(Axis.X, 3))
    )
    RIGHT_SHIFT = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=5, pin=ADG2128Pin(Axis.X, 4))
    )
    PERIOD = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=6, pin=ADG2128Pin(Axis.X, 5))
    )
    RIGHT_FUNCTION = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=7, pin=ADG2128Pin(Axis.Y, 0))
    )
    NUMPAD_6 = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=10, pin=ADG2128Pin(Axis.Y, 3))
    )
    DOWN = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=12, pin=ADG2128Pin(Axis.Y, 5))
    )
    SPACE = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=13, pin=ADG2128Pin(Axis.Y, 6))
    )
    NUMPAD_ENTER = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=22, pin=ADG2128Pin(Axis.X, 11))
    )
    NUMPAD_PERIOD = Mapping(
        row=Pin(i2c_addr=ROW_I2C_ADDR, logi_pin=21, pin=ADG2128Pin(Axis.Y, 4)),
        col=Pin(i2c_addr=COL_I2C_ADDR, logi_pin=24, pin=ADG2128Pin(Axis.X, 9))
    )