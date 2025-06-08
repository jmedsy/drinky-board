import serial.tools.list_ports

class PicoDevice:
    # region Conastants
    VID_PID = [
        (0x2e8a, 0x0005),  # RP2040 USB Serial
        (0x2e8a, 0x0003),  # Pico in CDC ACM mode
    ]
    DEFAULT_BAUDRATE = 115200
    DEFAULT_TIMEOUT = 1
    #endregion

    @staticmethod
    def find_pico_ports():
        pico_ports = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            desc = port.description.lower()
            vid = port.vid
            pid = port.pid
            if (
                'pico' in desc or
                (vid, pid) in PicoDevice.VID_PID
            ):
                pico_ports.append(port.device)
        return pico_ports