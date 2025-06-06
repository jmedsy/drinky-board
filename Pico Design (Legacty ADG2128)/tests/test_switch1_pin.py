from machine import I2C, Pin
import time

# I2C setup (GPIO 0 = SDA, GPIO 1 = SCL)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)

# I2C address of ADG2128 (change if A0–A2 are wired differently)
ADG2128_ADDR = 0x70  # default if A0=A1=A2=0

def connect_switch(x, y):
    """Connect Xn to Ym (0 ≤ x ≤ 11, 0 ≤ y ≤ 7)"""
    if not (0 <= x <= 11 and 0 <= y <= 7):
        print("❌ Invalid X or Y pin number.")
        return

    command = (x << 3) | y
    try:
        i2c.writeto(ADG2128_ADDR, bytes([command]))
        print(f"✅ Connected X{x} to Y{y}")
    except Exception as e:
        print(f"❌ Failed to connect X{x} to Y{y}: {e}")

# Replace these with the pin combo you’re testing with the meter
connect_switch(0, 0)  # Example: Connect X0 to Y0
