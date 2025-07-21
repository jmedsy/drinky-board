from flask import Blueprint, jsonify, request
from logic.sequences_manager import (
    load_all_sequences, load_sequence, save_sequence, delete_sequence,
    add_sequence, edit_sequence, deactivate_all_except
)

bp = Blueprint('sequences', __name__, url_prefix='/sequences')

@bp.route('/get_all')
def get_all():
    try:
        sequences = load_all_sequences()
        return jsonify({
            'message': 'Sequences loaded successfully',
            'success': True,
            'sequences': sequences
        })
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500

@bp.route('/add', methods=['POST'])
def add():
    try:
        sequence_data = request.get_json()
        if not sequence_data:
            return jsonify({
                'message': 'No sequence data provided',
                'success': False
            }), 400
        required_fields = ['name', 'wpm', 'wpmVariation', 'keyDuration', 'keyDurationVariation', 'isActive']
        for field in required_fields:
            if field not in sequence_data:
                return jsonify({
                    'message': f'Missing required field: {field}',
                    'success': False
                }), 400
        filename = add_sequence(sequence_data)
        return jsonify({
            'message': 'Sequence added successfully',
            'success': True,
            'filename': filename,
            'sequence': sequence_data
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
        deleted = delete_sequence(filename)
        if not deleted:
            return jsonify({
                'message': 'Sequence not found',
                'success': False
            }), 404
        return jsonify({
            'message': 'Sequence deleted successfully',
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
        sequence_data = request.get_json()
        if not sequence_data:
            return jsonify({
                'message': 'No sequence data provided',
                'success': False
            }), 400
        required_fields = ['name', 'wpm', 'wpmVariation', 'keyDuration', 'keyDurationVariation', 'isActive']
        for field in required_fields:
            if field not in sequence_data:
                return jsonify({
                    'message': f'Missing required field: {field}',
                    'success': False
                }), 400
        edited = edit_sequence(filename, sequence_data)
        if not edited:
            return jsonify({
                'message': 'Sequence not found or corrupted',
                'success': False
            }), 404
        return jsonify({
            'message': 'Sequence updated successfully',
            'success': True,
            'filename': filename,
            'sequence': sequence_data
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
                'message': 'No sequences updated (target not found?)',
                'success': False
            }), 404
        return jsonify({
            'message': f'Successfully updated {updated_count} sequences. Only {filename} is now active.',
            'success': True,
            'active_sequence': filename,
            'sequences_updated': updated_count
        })
    except Exception as e:
        return jsonify({
            'message': str(e),
            'success': False
        }), 500