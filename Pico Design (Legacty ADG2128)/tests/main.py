from machine import I2C, Pin
import sys

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)
ADDR = 0x70

def connect_switch(x, y):
    command = (x << 3) | y
    i2c.writeto(ADDR, bytes([command]))

while True:
    line = sys.stdin.readline().strip()
    if line.startswith("connect_switch"):
        try:
            _, x, y = line.split()
            connect_switch(int(x), int(y))
            print("OK")
        except Exception as e:
            print(f"ERR: {e}")
