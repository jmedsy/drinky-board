from flask import Blueprint, jsonify, request
from logic.preferences_manager import load_preferences, save_preferences, get_default_preferences

bp = Blueprint('preferences', __name__, url_prefix='/preferences')

@bp.route('/get', methods=['GET'])
def get_preferences():
    '''Get all user preferences'''
    try:
        preferences = load_preferences()
        return jsonify({
            'message': 'Preferences loaded successfully',
            'success': True,
            'preferences': preferences
        })
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500

@bp.route('/update', methods=['PUT'])
def update_preferences():
    '''Update user preferences'''
    try:
        preferences = load_preferences()
        updates = request.get_json()
        
        if not updates:
            return jsonify({
                'message': 'No preference data provided',
                'success': False
            }), 400
        
        # Merge updates with existing preferences
        preferences.update(updates)
        
        # Save updated preferences
        save_preferences(preferences)
        
        return jsonify({
            'message': 'Preferences updated successfully',
            'success': True,
            'preferences': preferences
        })
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500

@bp.route('/update_profile_order', methods=['PUT'])
def update_profile_order():
    '''Update the order of profiles in the UI'''
    try:
        preferences = load_preferences()
        profile_order = request.get_json()
        
        if not isinstance(profile_order, list):
            return jsonify({
                'message': 'Profile order must be a list',
                'success': False
            }), 400
        
        preferences['profileOrder'] = profile_order
        save_preferences(preferences)
        
        return jsonify({
            'message': 'Profile order updated successfully',
            'success': True,
            'profileOrder': profile_order
        })
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500
    
@bp.route('/update_sequence_order', methods=['PUT'])
def update_sequence_order():
    '''Update the order of sequences in the UI'''
    try:
        preferences = load_preferences()
        sequence_order = request.get_json()
        
        if not isinstance(sequence_order, list):
            return jsonify({
                'message': 'Sequence order must be a list',
                'success': False
            }), 400
        
        preferences['sequenceOrder'] = sequence_order
        save_preferences(preferences)
        
        return jsonify({
            'message': 'Sequence order updated successfully',
            'success': True,
            'sequenceOrder': sequence_order
        })
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500

@bp.route('/reset', methods=['POST'])
def reset_preferences():
    '''Reset preferences to defaults'''
    try:
        default_prefs = get_default_preferences()
        save_preferences(default_prefs)
        
        return jsonify({
            'message': 'Preferences reset to defaults',
            'success': True,
            'preferences': default_prefs
        })
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500 