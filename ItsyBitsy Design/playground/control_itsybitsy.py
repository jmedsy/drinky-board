import serial
import time

# Configure the serial port
# You might need to change the port name depending on your system
# Common port names:
# - Windows: 'COM3', 'COM4', etc.
# - Mac: '/dev/tty.usbmodem*' or '/dev/tty.usbserial*'
# - Linux: '/dev/ttyUSB0' or '/dev/ttyACM0'
PORT = '/dev/tty.usbmodem101'  # Change this to match your system
BAUD_RATE = 9600

def send_command(ser, pin, state):
    """Send a command to the ItsyBitsy."""
    command = f"{pin},{state}\n"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    print(f"Sent: {command.strip()}")
    print(f"Received: {response}")

def main():
    try:
        # Open serial port
        ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for Arduino to reset
        
        print("Connected to ItsyBitsy")
        print("Sending test commands...")
        
        # Example: Toggle pin 13 (usually the built-in LED)
        send_command(ser, 13, "HIGH")
        time.sleep(1)
        send_command(ser, 13, "LOW")
        
        # Keep the connection open for manual testing
        print("\nEnter commands manually (pin,state) or 'q' to quit:")
        while True:
            cmd = input("> ").strip()
            if cmd.lower() == 'q':
                break
                
            try:
                pin, state = cmd.split(',')
                send_command(ser, pin, state)
            except ValueError:
                print("Invalid command format. Use: pin,state (e.g., 13,HIGH)")
                
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed")

if __name__ == "__main__":
    main() 