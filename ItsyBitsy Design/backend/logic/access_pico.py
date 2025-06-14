# example for sending instructions to the pico

import serial

ser = serial.Serial('/dev/ttyACM0', 115200)
ser.write(b'U1,A,5\n')  # Send switch command
