import serial.tools.list_ports
import serial
import struct
from logic.keymaps.physical_map import KEYS

class ItsyBitsyDevice:
    # region Constants
    VID_PID = [
        (0x239A, 0x8001), # Adafruit ItsyBitsy 32u4
    ]
    DEFAULT_BAUDRATE = 115200
    DEFAULT_TIMEOUT = 0.001
    #endregion

    def __init__(self, port: str):
        self.port = port
        self.ser = serial.Serial(
            port,
            self.DEFAULT_BAUDRATE,
            timeout=self.DEFAULT_TIMEOUT
        )

    @classmethod
    def find_devices(cls):
        devices = []
        for port in serial.tools.list_ports.comports():
            if 'itsybitsy' in port.description.lower() or (port.vid, port.pid) in cls.VID_PID:
                try:
                    devices.append(cls(port.device))
                except Exception as e:
                    print(f'Failed to connect to {port.device}: {e}')
        return devices
    
    def send_command(self, key, action):
        if (
            self is not None and 
            getattr(self, 'ser', None) and 
            self.ser.is_open
        ):
            command = struct.pack('>BBBBBBBBBBBBB',
                key.row.i2c_addr,
                key.row.logi_pin,
                key.row.pin.axis.value,
                key.row.pin.channel,
                key.row.bus_pin.axis.value,
                key.row.bus_pin.channel,
                key.col.i2c_addr,
                key.col.logi_pin,
                key.col.pin.axis.value,
                key.col.pin.channel,
                key.col.bus_pin.axis.value,
                key.col.bus_pin.channel,
                1 if action == 'PRESS' else 0
            )
            self.ser.write(command)
            self.ser.flush()

    def close(self):
        if self.ser.is_open:
            print(f'Closing device on port {self.port}')
            self.ser.close()