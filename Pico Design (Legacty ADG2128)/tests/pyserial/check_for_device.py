# read_itsybitsy.py
import serial
import time

PORT = "/dev/tty.usbmodem101"
BAUDRATE = 9600

with serial.Serial(PORT, BAUDRATE, timeout=1) as ser:
    time.sleep(2)  # Allow board to reset
    print("🕵️ Listening for messages...")
    for _ in range(10):
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if line:
            print("✅ Received:", line)
        time.sleep(1)
