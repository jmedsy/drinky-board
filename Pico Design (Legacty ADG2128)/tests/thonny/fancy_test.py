from machine import I2C, Pin
import time

# Setup I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)
addr = 0x70  # ADG2128 default I2C address

x = 6  # X6 = pin 17

print("Beginning test of X6 (pin 17) to ALL Y pins (pins 9–16)...")

for y in range(1):  # Y0–Y7 = pins 9–16
    ax = x
    ay = 1
    middle = 0b10000000 | (ax << 3) | ay

    print(f"\n🔗 Connecting X{ax} (pin 17) to Y{ay} (pin {9 + y})")
    print(f"→ Command: connect → [0x{middle:02X}, 0x01] = {list(bytes([middle, 0x01]))}")

    # Special case: X6 ↔ Y2 = pin 17 ↔ pin 11
    if ay == 2:
        input("\n⏸️ Ready to connect pin 17 ↔ 11. Press Enter to proceed...")

    try:
        i2c.writeto(addr, bytes([middle, 0x01]))
    except Exception as e:
        print(f"❌ Connect error: {e}")

    if ay == 2:
        input("⏸️ Connection active (X6 ↔ Y2). Probe now. Press Enter to disconnect...")
        print("  [Debug] Still connected... nothing is writing to chip right now.")

    print(f"→ Command: disconnect → [0x{middle:02X}, 0x02] = {list(bytes([middle, 0x02]))}")
    try:
        i2c.writeto(addr, bytes([middle, 0x02]))
    except Exception as e:
        print(f"❌ Disconnect error: {e}")

    if ay == 2:
        input("⏸️ Disconnected. Probe again if needed. Press Enter to continue...\n")
    else:
        time.sleep(0.5)

print("\n✅ Finished sweeping all Y pins on X6.")

