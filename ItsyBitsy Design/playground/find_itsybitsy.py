import serial.tools.list_ports
import serial
import time

def find_itsybitsy():
    # List all available ports
    print("Available ports:")
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"  {port.device} - {port.description}")
    
    # Try to find the ItsyBitsy
    print("\nTrying to connect to ItsyBitsy...")
    for port in ports:
        if "usbmodem" in port.device.lower():
            try:
                print(f"\nAttempting to connect to {port.device}...")
                ser = serial.Serial(port.device, 9600, timeout=1)
                time.sleep(2)  # Wait for Arduino to reset
                
                # Try to read any initial output
                if ser.in_waiting:
                    print("Received:", ser.readline().decode().strip())
                
                print("Successfully connected!")
                ser.close()
                return port.device
            except Exception as e:
                print(f"Failed to connect: {e}")
    
    return None

if __name__ == "__main__":
    port = find_itsybitsy()
    if port:
        print(f"\nItsyBitsy found at: {port}")
    else:
        print("\nNo ItsyBitsy found. Make sure it's connected and not in use by another program.") 