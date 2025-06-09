from flask import Flask, jsonify
from flask_cors import CORS
from routes import find_pico_ports

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

# Register blueprints
app.register_blueprint(find_pico_ports.bp)

# CORS
if __name__ == '__main__':
    app.run(host='localhost', port=5050)