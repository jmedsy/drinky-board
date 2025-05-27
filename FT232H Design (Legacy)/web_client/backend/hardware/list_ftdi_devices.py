from pyftdi.ftdi import Ftdi

print("Detecting FTDI devices...")
devices = list(Ftdi.show_devices())

return devices
