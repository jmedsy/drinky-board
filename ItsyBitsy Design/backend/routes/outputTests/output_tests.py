from flask import Blueprint, jsonify
from logic.itsybitsy_device import ItsyBitsyDevice
from logic.keymaps.physical_map import KEYS
from logic.keygroup.keygroup import get_keymap_name
import serial
import struct
from time import sleep

output_tests_bp = Blueprint('output_tests', __name__, url_prefix='/outputTests')

def send_command(ser, key, action):
    """Send a command to the Arduino"""
    command = struct.pack('>BBBBBBBBBBBBB',
        key.row.i2c_addr,
        key.row.logi_pin,
        key.row.pin.axis.value,
        key.row.pin.channel,
        key.row.bus_pin.axis.value,
        key.row.bus_pin.channel,
        key.col.i2c_addr,
        key.col.logi_pin,
        key.col.pin.axis.value,
        key.col.pin.channel,
        key.col.bus_pin.axis.value,
        key.col.bus_pin.channel,
        1 if action == "PRESS" else 0
    )
    ser.write(command)
    ser.flush()

@output_tests_bp.route('/alphabet')
def output_tests():
    try:
        ports = ItsyBitsyDevice.find_itsybitsy_ports()
        ser = serial.Serial(ports[0], 115200, timeout=0.001)

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for letter in alphabet:
            keymap = getattr(KEYS, letter.capitalize())
            if keymap is not None:
                send_command(ser, keymap, 'PRESS')
                sleep(0.02)
                send_command(ser, keymap, 'RELEASE')
                sleep(0.02)
        return jsonify({
            'message': 'Performed output test: "Alphabet"',
            'success': True
        }) 
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500
