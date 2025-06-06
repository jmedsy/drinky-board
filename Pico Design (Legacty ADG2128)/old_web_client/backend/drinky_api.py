from flask import Flask, request, jsonify
from flask_cors import CORS
from one_key.routes import one_key_api

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

app.register_blueprint(one_key_api, url_prefix='/flask_api')

# @app.route('/flask-api/send-text', methods=['POST'])
# def receive_text():
#     data = request.get_json()
#     text = data.get('text', '')

#     print(f"Received text from frontend:\n{text}")

#     # type_text_to_matrix(text)

#     return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=8000)