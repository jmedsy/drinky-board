from machine import I2C, Pin
import time

# Setup I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)
addr = 0x70  # ADG2128 default I2C address

print("Disconnecting ALL 128 switches (X0–X7 to Y0–Y15)...")

for x in range(8):       # X0 to X7
    for y in range(16):  # Y0 to Y15
        middle = 0b10000000 | (x << 3) | y
        print(f"→ Send: [0x{middle:02X}, 0x02]  (X{x} ↔ Y{y} disconnect)")
        try:
            i2c.writeto(addr, bytes([middle, 0x02]))
            time.sleep(0.01)  # brief pause between commands
        except Exception as e:
            print(f"❌ I2C error on X{x} Y{y}: {e}")

print("✅ All crosspoints should now be disconnected.")

