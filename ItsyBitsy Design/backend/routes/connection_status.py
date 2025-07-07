from flask import Blueprint, jsonify

bp = Blueprint('connection_status', __name__)

def get_itsy_device():
    import app
    return app.itsy_device

@bp.route('/connection_status')
def connection_status():
    itsy_device = get_itsy_device()
    
    print(f'Connection status check - Device: {itsy_device}')
    print(f'Device port: {itsy_device.port if itsy_device else "None"}')
    
    if not itsy_device:
        print('No device found')
        return jsonify({
            'connected': False,
            'status': 'disconnected',
            'message': 'No device found',
            'port': None,
            'last_heartbeat': None
        })
    
    # Check if device is actually connected and responsive
    is_connected = itsy_device.is_connected()
    print(f'Device on {itsy_device.port} - Connected: {is_connected}')
    
    if is_connected:
        print('Returning connected status')
        return jsonify({
            'connected': True,
            'status': 'connected',
            'message': f'Device connected on port {itsy_device.port}',
            'port': itsy_device.port,
            'last_heartbeat': itsy_device.last_heartbeat
        })
    else:
        print('Returning unresponsive status')
        return jsonify({
            'connected': False,
            'status': 'unresponsive',
            'message': f'Device on port {itsy_device.port} is not responding',
            'port': itsy_device.port,
            'last_heartbeat': itsy_device.last_heartbeat
        }) 