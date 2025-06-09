# Flash Pico with Thonny

from machine import Pin
import sys

# === PIN CONFIG ===
BUS = {
    'A0': Pin(0, Pin.OUT),
    'A1': Pin(1, Pin.OUT),
    'A2': Pin(2, Pin.OUT),
    'A3': Pin(3, Pin.OUT),
    'WR': Pin(4, Pin.OUT),
    # 'EN': Pin(5, Pin.OUT)  # optional if you want EN control
}

CHIPS = {
    'U1': {
        'CSA': Pin(10, Pin.OUT),
        'CSB': Pin(11, Pin.OUT),
    },
    'U2': {
        'CSA': Pin(12, Pin.OUT),
        'CSB': Pin(13, Pin.OUT),
    },
}

def set_address(index):
    """Set A0–A3 to the binary value of index (0–15)."""
    for i, bit in enumerate(['A0', 'A1', 'A2', 'A3']):
        BUS[bit].value((index >> i) & 1)

def pulse_wr():
    BUS['WR'].value(0)
    BUS['WR'].value(1)

def activate_switch(chip, side, pin_index):
    """Latch a switch connection on a specific chip and side."""
    set_address(pin_index)
    cs = CHIPS[chip][f'CS{side}']
    cs.value(0)
    pulse_wr()
    cs.value(1)  # optional: release CS

# === SERIAL LOOP ===
print("Ready to receive commands...")

while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:
            continue

        # Expect: U1,A,5
        parts = line.split(',')
        if len(parts) != 3:
            print("Invalid input:", line)
            continue

        chip, side, pin_str = parts
        pin_index = int(pin_str)

        if chip not in CHIPS or side not in ('A', 'B') or not (0 <= pin_index <= 15):
            print("Invalid command:", line)
            continue

        activate_switch(chip, side, pin_index)
        print("OK:", line)

    except Exception as e:
        print("ERR:", str(e))
