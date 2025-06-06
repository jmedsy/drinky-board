import serial.tools.list_ports

def find_pico_port():
    for port in serial.tools.list_ports.comports():
        if port.vid == 0x2E8A and port.pid == 0x0005:
            print('foo')
            return port.device
        else:
            print('bar')
    raise RuntimeError("Raspberry Pi Pico not found.")

find_pico_port()