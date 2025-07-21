from flask import Blueprint, jsonify, request
from logic.profiles_manager import (
    load_all_profiles, load_profile, save_profile, delete_profile,
    add_profile, edit_profile, deactivate_all_except
)

bp = Blueprint('profiles', __name__, url_prefix='/profiles')

@bp.route('/get_all')
def get_all():
    try:
        profiles = load_all_profiles()
        return jsonify({
            'message': 'Profiles loaded successfully',
            'success': True,
            'profiles': profiles
        })
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500

@bp.route('/add', methods=['POST'])
def add():
    try:
        profile_data = request.get_json()
        if not profile_data:
            return jsonify({
                'message': 'No profile data provided',
                'success': False
            }), 400
        required_fields = ['name', 'wpm', 'wpmVariation', 'keyDuration', 'keyDurationVariation', 'isActive']
        for field in required_fields:
            if field not in profile_data:
                return jsonify({
                    'message': f'Missing required field: {field}',
                    'success': False
                }), 400
        filename = add_profile(profile_data)
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
        if not filename.endswith('.json'):
            return jsonify({
                'message': 'Invalid filename',
                'success': False
            }), 400
        deleted = delete_profile(filename)
        if not deleted:
            return jsonify({
                'message': 'Profile not found',
                'success': False
            }), 404
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
        if not filename.endswith('.json'):
            return jsonify({
                'message': 'Invalid filename',
                'success': False
            }), 400
        profile_data = request.get_json()
        if not profile_data:
            return jsonify({
                'message': 'No profile data provided',
                'success': False
            }), 400
        required_fields = ['name', 'wpm', 'wpmVariation', 'keyDuration', 'keyDurationVariation', 'isActive']
        for field in required_fields:
            if field not in profile_data:
                return jsonify({
                    'message': f'Missing required field: {field}',
                    'success': False
                }), 400
        edited = edit_profile(filename, profile_data)
        if not edited:
            return jsonify({
                'message': 'Profile not found or corrupted',
                'success': False
            }), 404
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
        if not filename.endswith('.json'):
            return jsonify({
                'message': 'Invalid filename',
                'success': False
            }), 400
        updated_count = deactivate_all_except(filename)
        if updated_count == 0:
            return jsonify({
                'message': 'No profiles updated (target not found?)',
                'success': False
            }), 404
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