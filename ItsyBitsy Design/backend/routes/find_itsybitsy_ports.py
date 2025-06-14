from flask import Blueprint, jsonify
from logic.itsybitsy_device import ItsyBitsyDevice

bp = Blueprint('find_itsybitsy_ports', __name__)

@bp.route('/find_itsybitsy_ports')
def find_itsybitsy_ports():
    ports = ItsyBitsyDevice.find_itsybitsy_ports()
    if ports:
        return jsonify({
            'message': f'ItsyBitsy connected on port(s): {", ".join(ports)}',
            'success': True,
            'ports': ports
        })
    else:
        return jsonify({
            'message': "No ItsyBitsy devices found. Make sure it's connected and not in use by another program.",
            'success': False,
            'ports': []
        }) 