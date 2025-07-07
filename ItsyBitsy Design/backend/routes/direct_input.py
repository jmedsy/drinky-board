from flask import Blueprint, jsonify, request
from logic.keymaps.key_definitions import KEYS
from time import sleep

bp = Blueprint('direct_input', __name__, url_prefix='/direct_input')

def get_itsy_device():
    import app
    return app.itsy_device

@bp.route('/listen', methods=['GET', 'POST'])
def direct_input():
    import app
    try:
        itsy_device = get_itsy_device()

        def handleModifier(modifier: str, action: str):
            if modifier in ['ControlLeft', 'ControlRight']:
                itsy_device.send_command(KEYS.LEFT_CTRL, action)
            elif modifier in ['ShiftLeft', 'ShiftRight']:
                itsy_device.send_command(KEYS.LEFT_SHIFT, action)
            elif modifier in ['AltLeft', 'AltRight']:
                itsy_device.send_command(KEYS.LEFT_ALT, action)
            elif modifier in ['MetaLeft', 'MetaRight']:
                itsy_device.send_command(KEYS.LEFT_WINDOWS, action)

        if request.method == 'POST':
            # Handle POST request with key data
            data = request.get_json()
            code = data.get('code', '')
            additional_data = data.get('data', [])
            event_type = data.get('type', 'keydown')  # 'keydown' or 'keyup'
            
            # Handle modifier keys
            modifier_keys = {'ControlLeft', 'ControlRight', 'ShiftLeft', 'ShiftRight', 'AltLeft', 'AltRight', 'MetaLeft', 'MetaRight'}
            if code in modifier_keys:
                if event_type == 'keydown':
                    app.active_modifiers.add(code)
                    handleModifier(code, 'PRESS')
                elif event_type == 'keyup':
                    app.active_modifiers.discard(code)
                    handleModifier(code, 'RELEASE')
                print(f"Modifier state: {app.active_modifiers}")
                return jsonify({
                    'message': f'Modifier key {code} {event_type}',
                    'success': True,
                    'code': code,
                    'modifiers': list(app.active_modifiers)
                })
            
            # Search through KEYS object to find matching key
            matching_key = None
            matching_key_obj = None
            for key_name, key_obj in vars(KEYS).items():
                if hasattr(key_obj, 'string_aliases') and hasattr(key_obj.string_aliases, 'web_client'):
                    if code in key_obj.string_aliases.web_client:
                        matching_key = key_name
                        matching_key_obj = key_obj
                        break
            
            if matching_key:
                print(f"Found matching key: {matching_key}")

                # Send device no commands (as of current hardware design) for non-modifier keyup events
                if event_type == 'keyup':
                    return jsonify({
                        'message': f'Found matching key: {matching_key}, performed no action for event {event_type}',
                        'success': True,
                        'code': code,
                        'modifiers': list(app.active_modifiers)
                    })

                # Check if command was sent successfully (PRESS)
                if not itsy_device.send_command(matching_key_obj, 'PRESS'):
                    return jsonify({
                        'message': 'Device disconnected',
                        'success': False,
                        'device_disconnected': True
                    }), 500
                sleep(0.02)

                # Check if command was sent successfully (RELEASE)
                if not itsy_device.send_command(matching_key_obj, 'RELEASE'):
                    return jsonify({
                        'message': 'Device disconnected',
                        'success': False,
                        'device_disconnected': True
                    }), 500
                sleep(0.02)

                # Only return success if both commands succeeded
                return jsonify({
                    'message': f'Found matching key: {matching_key}',
                    'success': True,
                    'code': code,
                    'matching_key': matching_key,
                    'data': additional_data,
                    'modifiers': list(app.active_modifiers)
                })
            else:
                print(f"No matching key found for code: {code}")
                return jsonify({
                    'message': f'No matching key found for code: {code}',
                    'success': False,
                    'code': code,
                    'data': additional_data
                })
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500
