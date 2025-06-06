import serial

# Replace with the actual port if different
PORT = '/dev/cu.usbmodem101'

def send_switch_command(x, y):
    with serial.Serial(PORT, 115200, timeout=1) as ser:
        # Send the command
        command = f'connect_switch {x} {y}\n'
        ser.write(command.encode('utf-8'))

        # Read response
        response = ser.readline().decode('utf-8').strip()
        print(f"Pico response: {response}")

if __name__ == "__main__":
    send_switch_command(3, 4)
