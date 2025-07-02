from flask import Flask, jsonify
from flask_cors import CORS
from routes import find_itsybitsy_ports
from routes.outputTests import output_tests_bp

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

# Register blueprints
app.register_blueprint(find_itsybitsy_ports.bp)
app.register_blueprint(output_tests_bp)

# CORS
if __name__ == '__main__':
    app.run(host='localhost', port=5050)