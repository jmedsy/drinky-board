from flask import Blueprint, jsonify
from logic.keymaps.physical_map import KEYS
from time import sleep

output_tests_bp = Blueprint('output_tests', __name__, url_prefix='/outputTests')

def get_itsy_device():
    import app
    return app.itsy_device

@output_tests_bp.route('/alphabet')
def output_tests():
    try:
        itsy_device = get_itsy_device()

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for letter in alphabet:
            keymap = getattr(KEYS, letter.capitalize())
            if keymap is not None:
                itsy_device.send_command(keymap, 'PRESS')
                sleep(0.02)
                itsy_device.send_command(keymap, 'RELEASE')
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
