from pyftdi.gpio import GpioController
import time

SCL = 0x01  # D0
SDA = 0x02  # D1
BOTH = SCL | SDA

gpio = GpioController()
gpio.configure('ftdi://ftdi:232h/1', direction=BOTH)

def delay():
    time.sleep(0.00001)  # 10 microseconds

def sda_high():
    gpio.set_direction(BOTH, SCL)  # SDA = input
    delay()

def sda_low():
    gpio.set_direction(BOTH, BOTH)  # SDA = output
    gpio.write(gpio.read() & ~SDA)
    delay()

def scl_high():
    gpio.write(gpio.read() | SCL)
    delay()

def scl_low():
    gpio.write(gpio.read() & ~SCL)
    delay()

def i2c_start():
    sda_high()
    scl_high()
    sda_low()
    scl_low()

def i2c_stop():
    sda_low()
    scl_high()
    sda_high()

def write_byte(byte):
    for i in range(8):
        if (byte & 0x80):
            sda_high()
        else:
            sda_low()
        byte <<= 1
        scl_high()
        scl_low()
    # ACK bit (from slave)
    sda_high()  # release SDA
    scl_high()
    ack = gpio.read() & SDA
    scl_low()
    return ack == 0

# 🧪 Try it
i2c_start()
ack = write_byte(0x4E)  # MCP23017 write addr = 0x27 << 1 | 0
print("ACK received" if ack else "NACK")
i2c_stop()
