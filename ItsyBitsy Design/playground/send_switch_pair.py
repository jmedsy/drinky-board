import serial
import time

def main():
    port = '/dev/tty.usbmodem101'  # Updated port name
    baud = 115200

    try:
        ser = serial.Serial(port, baud, timeout=2)
        time.sleep(2)  # Wait for Arduino to boot/reset

        while True:
            line = input("Enter pair like '1,2 3,4' or 'q' to quit: ").strip()
            if line.lower() in ('q', 'quit', 'exit'):
                break
            if ',' not in line or ' ' not in line:
                print("Bad format. Use: row1,col1 row2,col2")
                continue

            ser.write((line + '\n').encode('utf-8'))
            print("Sent:", line)

    except serial.SerialException as e:
        print("Serial error:", e)
    except KeyboardInterrupt:
        pass
    finally:
        if 'ser' in locals():
            ser.close()
        print("Exiting.")

if __name__ == "__main__":
    main()
