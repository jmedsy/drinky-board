import os
import json
import uuid
from datetime import datetime
from logic.preferences_manager import load_preferences, save_preferences

SEQUENCES_DIR = 'data/sequences'

# Utility to ensure the sequences directory exists
def ensure_sequences_dir():
    if not os.path.exists(SEQUENCES_DIR):
        os.makedirs(SEQUENCES_DIR)

# Load all sequences, optionally sorted by sequenceOrder from preferences
def load_all_sequences():
    ensure_sequences_dir()
    sequences = []
    for filename in os.listdir(SEQUENCES_DIR):
        if filename.endswith('.json'):
            file_path = os.path.join(SEQUENCES_DIR, filename)
            try:
                with open(file_path, 'r') as f:
                    sequence_data = json.load(f)
                    sequences.append({'filename': filename, 'data': sequence_data})
            except json.JSONDecodeError:
                sequences.append({'filename': filename, 'error': 'Invalid JSON'})
    # Sort by sequenceOrder if available
    preferences = load_preferences()
    sequence_order = preferences.get('sequenceOrder', [])
    if sequence_order:
        order_map = {fn: i for i, fn in enumerate(sequence_order)}
        sequences.sort(key=lambda x: order_map.get(x['filename'], len(sequence_order)))
    return sequences

# Load a single sequence by filename
def load_sequence(filename):
    file_path = os.path.join(SEQUENCES_DIR, filename)
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        return json.load(f)

# Save a sequence (create or overwrite)
def save_sequence(filename, data):
    ensure_sequences_dir()
    file_path = os.path.join(SEQUENCES_DIR, filename)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

# Delete a sequence by filename
def delete_sequence(filename):
    file_path = os.path.join(SEQUENCES_DIR, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        # Remove from sequenceOrder in preferences
        preferences = load_preferences()
        sequence_order = preferences.get('sequenceOrder', [])
        if filename in sequence_order:
            sequence_order.remove(filename)
            preferences['sequenceOrder'] = sequence_order
            save_preferences(preferences)
        return True
    return False

# Add a new sequence (returns filename)
def add_sequence(sequence_data):
    ensure_sequences_dir()
    sequence_data['created'] = datetime.now().isoformat()
    filename = f"{uuid.uuid4()}.json"
    save_sequence(filename, sequence_data)
    # Add to sequenceOrder
    preferences = load_preferences()
    sequence_order = preferences.get('sequenceOrder', [])
    sequence_order.append(filename)
    preferences['sequenceOrder'] = sequence_order
    save_preferences(preferences)
    return filename

# Edit an existing sequence
def edit_sequence(filename, sequence_data):
    file_path = os.path.join(SEQUENCES_DIR, filename)
    if not os.path.exists(file_path):
        return False
    try:
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
            sequence_data['created'] = existing_data.get('created')
    except json.JSONDecodeError:
        return False
    save_sequence(filename, sequence_data)
    return True

# Deactivate all sequences except the given filename
def deactivate_all_except(filename):
    ensure_sequences_dir()
    updated_count = 0
    for sequence_filename in os.listdir(SEQUENCES_DIR):
        if sequence_filename.endswith('.json'):
            file_path = os.path.join(SEQUENCES_DIR, sequence_filename)
            try:
                with open(file_path, 'r') as f:
                    sequence_data = json.load(f)
                sequence_data['isActive'] = (sequence_filename == filename)
                with open(file_path, 'w') as f:
                    json.dump(sequence_data, f, indent=2)
                updated_count += 1
            except json.JSONDecodeError:
                continue
    return updated_count 