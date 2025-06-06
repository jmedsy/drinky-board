# scan_i2c.py
import serial
import time

PORT = "/dev/tty.usbmodem101"
BAUD = 9600

with serial.Serial(PORT, BAUD, timeout=2) as ser:
    time.sleep(2)  # Allow reset
    ser.write(b"SCAN\n")
    print("📡 Sent SCAN command, waiting for response...\n")
    while True:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if line:
            print(line)
        else:
            break
