from flask import Blueprint, jsonify
import os
import json

bp = Blueprint('profiles', __name__, url_prefix='/profiles')

# Path to the profiles directory (relative to Flask app working directory)
PROFILES_DIR = 'data/profiles'

@bp.route('/get_all')
def get_all():
    try:
        # Check if the directory exists
        if not os.path.exists(PROFILES_DIR):
            return jsonify({
                'message': 'Profiles directory not found',
                'success': False,
                'profiles': []
            }), 404
        
        # List all files in the profiles directory
        profile_files = []
        for filename in os.listdir(PROFILES_DIR):
            if filename.endswith('.json'):
                file_path = os.path.join(PROFILES_DIR, filename)
                try:
                    with open(file_path, 'r') as f:
                        profile_data = json.load(f)
                        profile_files.append({
                            'filename': filename,
                            'data': profile_data
                        })
                except json.JSONDecodeError:
                    profile_files.append({
                        'filename': filename,
                        'error': 'Invalid JSON'
                    })
        
        return jsonify({
            'message': 'Profiles loaded successfully',
            'success': True,
            'profiles': profile_files
        })
        
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500
