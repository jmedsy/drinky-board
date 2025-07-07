'''
ItsyBitsy Device Controller

This module provides the interface for communicating with the Adafruit ItsyBitsy 32u4
microcontroller that controls the Drinky Board keyboard matrix.

The ItsyBitsyDevice class handles:
- Serial communication with the ItsyBitsy microcontroller
- Device discovery and connection management
- Heartbeat monitoring to detect disconnections
- Sending key press/release commands to the hardware

Key Features:
- Automatic device discovery using USB VID/PID or port description
- Connection health monitoring with heartbeat checks
- Structured command protocol for key matrix control
- Error handling for serial communication issues

Usage:
- Find devices: devices = ItsyBitsyDevice.find_devices()
- Create connection: device = ItsyBitsyDevice(port)
- Send commands: device.send_command(KEYS.A, 'PRESS')
- Check connection: if device.is_connected(): ...
- Cleanup: device.close()

The device communicates using a binary protocol where each command contains
I2C addresses, pin assignments, and action (press/release) information.
'''

import serial.tools.list_ports
import serial
import struct
import time

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
        self.last_heartbeat = time.time()
        self.heartbeat_interval = 5.0  # Check every 5 seconds

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
    
    def is_connected(self):
        '''Check if device is actually connected and responsive'''
        if not self.ser or not self.ser.is_open:
            return False
        
        # Check if it's time for a heartbeat
        current_time = time.time()
        if current_time - self.last_heartbeat > self.heartbeat_interval:
            return self._send_heartbeat()
        
        return True
    
    def _send_heartbeat(self):
        '''Send a heartbeat command to verify device is responsive'''
        try:
            # Check if the port is still accessible and device is responsive
            if not self.ser.is_open:
                return False
            
            # Try to read any available data to see if device responds
            # This is a gentle way to test if the device is still there
            try:
                # This will fail if device is unplugged
                self.ser.in_waiting
                self.last_heartbeat = time.time()
                return True
            except (serial.SerialException, OSError):
                # Device is unplugged or unresponsive
                return False
                
        except (serial.SerialException, OSError) as e:
            print(f'Heartbeat failed: {e}')
            return False
    
    def send_command(self, key, action):
        if self.is_connected():
            try:
                command = struct.pack('>BBBBBBBBBBBBB',
                    key.physical_mapping.row.i2c_addr,
                    key.physical_mapping.row.logi_pin,
                    key.physical_mapping.row.pin.axis.value,
                    key.physical_mapping.row.pin.channel,
                    key.physical_mapping.row.bus_pin.axis.value,
                    key.physical_mapping.row.bus_pin.channel,
                    key.physical_mapping.col.i2c_addr,
                    key.physical_mapping.col.logi_pin,
                    key.physical_mapping.col.pin.axis.value,
                    key.physical_mapping.col.pin.channel,
                    key.physical_mapping.col.bus_pin.axis.value,
                    key.physical_mapping.col.bus_pin.channel,
                    1 if action == 'PRESS' else 0
                )
                self.ser.write(command)
                self.ser.flush()
            except (serial.SerialException, OSError) as e:
                print(f'Failed to send command: {e}')
                return False
        return True

    def close(self):
        if self.ser and self.ser.is_open:
            print(f'Closing device on port {self.port}')
            self.ser.close()