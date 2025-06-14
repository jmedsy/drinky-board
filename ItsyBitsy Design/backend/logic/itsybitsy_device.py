import serial.tools.list_ports
import serial
import time

class ItsyBitsyDevice:
    # region Constants
    VID_PID = [
        (0x239A, 0x8001),  # Adafruit ItsyBitsy 32u4
    ]
    DEFAULT_BAUDRATE = 9600
    DEFAULT_TIMEOUT = 1
    #endregion

    @staticmethod
    def find_itsybitsy_ports():
        """Find all available ItsyBitsy ports and test connection."""
        itsybitsy_ports = []
        ports = serial.tools.list_ports.comports()
        
        print("Available ports:")
        for port in ports:
            print(f"  {port.device} - {port.description}")
        
        print("\nTrying to connect to ItsyBitsy devices...")
        for port in ports:
            desc = port.description.lower()
            vid = port.vid
            pid = port.pid
            
            if 'itsybitsy' in desc or (vid, pid) in ItsyBitsyDevice.VID_PID:
                try:
                    print(f"\nAttempting to connect to {port.device}...")
                    ser = serial.Serial(
                        port.device, 
                        ItsyBitsyDevice.DEFAULT_BAUDRATE, 
                        timeout=ItsyBitsyDevice.DEFAULT_TIMEOUT
                    )
                    time.sleep(2)  # Wait for device to reset
                    
                    # Try to read any initial output
                    if ser.in_waiting:
                        print("Received:", ser.readline().decode().strip())
                    
                    print("Successfully connected!")
                    ser.close()
                    itsybitsy_ports.append(port.device)
                except Exception as e:
                    print(f"Failed to connect: {e}")
        
        return itsybitsy_ports

    @staticmethod
    def test_connection(port):
        """Test connection to a specific port."""
        try:
            ser = serial.Serial(
                port, 
                ItsyBitsyDevice.DEFAULT_BAUDRATE, 
                timeout=ItsyBitsyDevice.DEFAULT_TIMEOUT
            )
            time.sleep(2)
            
            # Try to read any initial output
            if ser.in_waiting:
                response = ser.readline().decode().strip()
                print(f"Received: {response}")
            
            ser.close()
            return True
        except Exception as e:
            print(f"Connection test failed: {e}")
            return False 