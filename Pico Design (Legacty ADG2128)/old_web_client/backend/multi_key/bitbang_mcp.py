# bitbang_mcp.py
from pyftdi.gpio import GpioController
import time

'''
Q. What is bit banging?
A. Bit banging is the practice of using software (this class) to emulate hardware-managed serial communication protocols.

Q. So how does this all work, exactly?
A. The FT232H is using its GPIO pins (instead of its I2C hardware) to communicate with the MCP23017 chips by way of bit banging. The MCP23017 registers are provided
   to us by its manufacturer datasheet (which I've included in /docs).

Q. Why the hell are we bit banging when the FT232H hardware natively supports the I2C protocol?
A. Unfortunately, MacOS does not play nice with the FTDI driver required for this. Fortunately, we can emulate I2C to control the MCP23017 chips with the FT232H.
       
   Bit Banging would probably not be necessary using a device with more complete driver support *cough raspberrypi*, but the FT232H is not that.
   Regardless, we would still need to know the MCP23017 addresses (which are included in this class as constants).

Q. How are we communicating with the FT232H?
A. We are using pyftdi which is a library for communicating with FTDI devices.
'''

class BitBangMCP:

    # region Constants (Pulled from MCP23017 datasheet)
    SCL = 0x01  # D0
    SDA = 0x02  # D1
    BOTH = SCL | SDA

    # CD4066BE (Switch) Bit Positions
    PALOW = PBLOW = 0b00000000
    PB0 = 0b00000001
    PB1 = 0b00000010
    PB2 = 0b00000100
    PB3 = 0b00001000
    PA4 = PB4 = 0b00010000
    PA5 = PB5 = 0b00100000
    PA6 = PB6 = 0b01000000
    PA7 = PB7 = 0b10000000

    # PA7= 0b10000000
    # endregion

    def __init__(self, address=0x27, url='ftdi://ftdi:232h/1'):
        self.address = address << 1
        self.gpio = GpioController()
        self.gpio.configure(url, direction=self.BOTH)
        self._set_sda_high()
        self._set_scl_high()

    def _delay(self):
        time.sleep(0.00001)  # 10 microseconds

    def _set_sda_high(self):
        self.gpio.set_direction(self.BOTH, self.SCL)  # SDA input
        self._delay()

    def _set_sda_low(self):
        self.gpio.set_direction(self.BOTH, self.BOTH)
        self.gpio.write(self.gpio.read() & ~self.SDA)
        self._delay()

    def _set_scl_high(self):
        self.gpio.write(self.gpio.read() | self.SCL)
        self._delay()

    def _set_scl_low(self):
        self.gpio.write(self.gpio.read() & ~self.SCL)
        self._delay()

    def _start(self):
        self._set_sda_high()
        self._set_scl_high()
        self._set_sda_low()
        self._set_scl_low()

    def _stop(self):
        self._set_sda_low()
        self._set_scl_high()
        self._set_sda_high()

    def _write_byte(self, byte):
        for i in range(8):
            if byte & 0x80:
                self._set_sda_high()
            else:
                self._set_sda_low()
            byte <<= 1
            self._set_scl_high()
            self._set_scl_low()
        self._set_sda_high()
        self._set_scl_high()
        ack = self.gpio.read() & self.SDA
        self._set_scl_low()
        return ack == 0

    def write_register(self, reg_addr, value):
        self._start()
        if not self._write_byte(self.address):
            raise RuntimeError("No ACK on address")
        if not self._write_byte(reg_addr):
            raise RuntimeError("No ACK on register")
        if not self._write_byte(value):
            raise RuntimeError("No ACK on data")
        self._stop()

    def close(self):
        self._stop()
        self.gpio.close()
        
    def read_register(self, reg_addr):
        self._start()
        if not self._write_byte(self.address):  # Write mode
            raise RuntimeError("No ACK on address (write)")
        if not self._write_byte(reg_addr):
            raise RuntimeError("No ACK on register")

        self._start()
        if not self._write_byte(self.address | 1):  # Read mode
            raise RuntimeError("No ACK on address (read)")

        value = 0
        for _ in range(8):
            self._set_scl_low()
            self._set_sda_high()  # SDA as input (set high = release)
            self._set_scl_high()
            bit = 1 if (self.gpio.read() & self.SDA) else 0
            value = (value << 1) | bit
        self._set_scl_low()

        # Send NACK
        self._set_sda_low()
        self._set_scl_high()
        self._set_scl_low()
        self._set_sda_high()

        self._stop()
        return value
