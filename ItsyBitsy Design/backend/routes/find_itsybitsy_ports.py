from flask import Blueprint, jsonify

bp = Blueprint('find_itsybitsy_ports', __name__)

def get_itsy_device():
    import app
    return app.itsy_device

@bp.route('/find_itsybitsy_ports')
def find_itsybitsy_ports():
    itsy_device = get_itsy_device()
    if itsy_device:
        return jsonify({
            'message': f'ItsyBitsy connected on port: {itsy_device.port}',
            'success': True,
            'port': itsy_device.port
        })
    else:
        return jsonify({
            'message': "No ItsyBitsy devices found. Make sure it's connected and not in use by another program.",
            'success': False,
            'port': None
        }) 