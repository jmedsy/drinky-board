import serial
import time

ser = serial.Serial("/dev/tty.usbmodem101", 9600, timeout=2)
time.sleep(2)  # Let ItsyBitsy boot

ser.write(b"PRESS A\n")
print("📨 Sent PRESS A command")

# Optionally read back any response
while ser.in_waiting:
    print(ser.readline().decode("utf-8").strip())

ser.close()
