from flask import Flask, jsonify
from flask_cors import CORS
from routes import hello

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

# Register blueprints
app.register_blueprint(hello.bp)

# CORS
if __name__ == '__main__':
    app.run(host='localhost', port=5050)