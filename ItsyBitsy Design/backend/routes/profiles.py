from flask import Blueprint, jsonify, request
import os
import json
import uuid
from datetime import datetime
from logic.preferences_manager import load_preferences

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
        
        # Get saved profile order from preferences
        preferences = load_preferences()
        profile_order = preferences.get('profileOrder', [])
        
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
        
        # Sort profiles according to saved order
        if profile_order:
            # Create a mapping of filename to index for sorting
            order_map = {filename: index for index, filename in enumerate(profile_order)}
            
            # Sort profile_files based on the order map
            # Files not in the order list will be placed at the end
            profile_files.sort(key=lambda x: order_map.get(x['filename'], len(profile_order)))
        
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

@bp.route('/add', methods=['POST'])
def add():
    try:
        # Check if the directory exists, create if it doesn't
        if not os.path.exists(PROFILES_DIR):
            os.makedirs(PROFILES_DIR)
        
        # Get profile data from request
        profile_data = request.get_json()
        
        if not profile_data:
            return jsonify({
                'message': 'No profile data provided',
                'success': False
            }), 400
        
        # Validate required fields
        required_fields = ['name', 'wpm', 'wpmVariation', 'keyDuration', 'keyDurationVariation', 'isActive']
        for field in required_fields:
            if field not in profile_data:
                return jsonify({
                    'message': f'Missing required field: {field}',
                    'success': False
                }), 400
        
        # Add creation timestamp
        profile_data['created'] = datetime.now().isoformat()
        
        # Generate unique filename using UUID4
        filename = f"{uuid.uuid4()}.json"
        file_path = os.path.join(PROFILES_DIR, filename)
        
        # Save profile to file
        with open(file_path, 'w') as f:
            json.dump(profile_data, f, indent=2)
        
        return jsonify({
            'message': 'Profile added successfully',
            'success': True,
            'filename': filename,
            'profile': profile_data
        })
        
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500

@bp.route('/delete/<filename>', methods=['DELETE'])
def delete(filename):
    try:
        # Validate filename (only allow .json files)
        if not filename.endswith('.json'):
            return jsonify({
                'message': 'Invalid filename',
                'success': False
            }), 400
        
        file_path = os.path.join(PROFILES_DIR, filename)
        
        # Check if file exists
        if not os.path.exists(file_path):
            return jsonify({
                'message': 'Profile not found',
                'success': False
            }), 404
        
        # Delete the file
        os.remove(file_path)
        
        return jsonify({
            'message': 'Profile deleted successfully',
            'success': True,
            'filename': filename
        })
        
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500

@bp.route('/edit/<filename>', methods=['PUT'])
def edit(filename):
    try:
        # Validate filename (only allow .json files)
        if not filename.endswith('.json'):
            return jsonify({
                'message': 'Invalid filename',
                'success': False
            }), 400
        
        file_path = os.path.join(PROFILES_DIR, filename)
        
        # Check if file exists
        if not os.path.exists(file_path):
            return jsonify({
                'message': 'Profile not found',
                'success': False
            }), 404
        
        # Get profile data from request
        profile_data = request.get_json()
        
        if not profile_data:
            return jsonify({
                'message': 'No profile data provided',
                'success': False
            }), 400
        
        # Validate required fields
        required_fields = ['name', 'wpm', 'wpmVariation', 'keyDuration', 'keyDurationVariation', 'isActive']
        for field in required_fields:
            if field not in profile_data:
                return jsonify({
                    'message': f'Missing required field: {field}',
                    'success': False
                }), 400
        
        # Load existing profile to preserve creation timestamp
        try:
            with open(file_path, 'r') as f:
                existing_data = json.load(f)
                profile_data['created'] = existing_data.get('created')  # Preserve original creation time
        except json.JSONDecodeError:
            return jsonify({
                'message': 'Existing profile file is corrupted',
                'success': False
            }), 500
        
        # Save updated profile to file
        with open(file_path, 'w') as f:
            json.dump(profile_data, f, indent=2)
        
        return jsonify({
            'message': 'Profile updated successfully',
            'success': True,
            'filename': filename,
            'profile': profile_data
        })
        
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500

@bp.route('/deactivateExcept/<filename>', methods=['PUT'])
def deactivate_except(filename):
    try:
        # Validate filename (only allow .json files)
        if not filename.endswith('.json'):
            return jsonify({
                'message': 'Invalid filename',
                'success': False
            }), 400
        
        # Check if the directory exists
        if not os.path.exists(PROFILES_DIR):
            return jsonify({
                'message': 'Profiles directory not found',
                'success': False
            }), 404
        
        # Check if the target profile exists
        target_file_path = os.path.join(PROFILES_DIR, filename)
        if not os.path.exists(target_file_path):
            return jsonify({
                'message': 'Target profile not found',
                'success': False
            }), 404
        
        # Process all profile files
        updated_count = 0
        for profile_filename in os.listdir(PROFILES_DIR):
            if profile_filename.endswith('.json'):
                file_path = os.path.join(PROFILES_DIR, profile_filename)
                try:
                    with open(file_path, 'r') as f:
                        profile_data = json.load(f)
                    
                    # Set isActive based on whether this is the target file
                    profile_data['isActive'] = (profile_filename == filename)
                    
                    # Save the updated profile
                    with open(file_path, 'w') as f:
                        json.dump(profile_data, f, indent=2)
                    
                    updated_count += 1
                    
                except json.JSONDecodeError:
                    # Skip corrupted files
                    continue
        
        return jsonify({
            'message': f'Successfully updated {updated_count} profiles. Only {filename} is now active.',
            'success': True,
            'active_profile': filename,
            'profiles_updated': updated_count
        })
        
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500