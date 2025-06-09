from flask import Blueprint, jsonify
from logic.pico_device import PicoDevice

bp = Blueprint('find_pico_ports', __name__)

@bp.route('/find_pico_ports')
def find_pico_ports():
    ports = PicoDevice.find_pico_ports()
    if len(ports) != 0:
        return jsonify(
            message=f'Pico connected on port(s): ' + ', '.join(ports),
            success=True
        )
    else:
        return jsonify(
            message="Device not found",
            success=False
        )