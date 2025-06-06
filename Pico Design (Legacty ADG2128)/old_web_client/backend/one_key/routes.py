from flask import Blueprint, request, jsonify

one_key_api = Blueprint('one_key_api', __name__)

@one_key_api.route('/one_key/trigger_once', methods=['POST'])
def trigger_key():
    print('googoo')
    return jsonify({'status': 'foo'})
    # data = request.get_json()
    # key = data.get('key', '')
    # print(f"Triggering key: {key}")
    # return jsonify({'status': 'triggered', 'key': key})
