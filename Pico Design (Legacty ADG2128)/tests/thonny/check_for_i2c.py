from machine import I2C, Pin
import time

# Set up I2C0 on GPIO 0 (SDA), GPIO 1 (SCL)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)

while True:
    devices = i2c.scan()
    if devices:
        print("I2C device(s) found at:", [hex(dev) for dev in devices])
    else:
        print("No I2C devices found.")
    time.sleep(2)


