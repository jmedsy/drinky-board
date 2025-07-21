import os
import json
import uuid
from datetime import datetime
from logic.preferences_manager import load_preferences, save_preferences

PROFILES_DIR = 'data/profiles'

# Utility to ensure the profiles directory exists
def ensure_profiles_dir():
    if not os.path.exists(PROFILES_DIR):
        os.makedirs(PROFILES_DIR)

# Load all profiles, optionally sorted by profileOrder from preferences
def load_all_profiles():
    ensure_profiles_dir()
    profiles = []
    for filename in os.listdir(PROFILES_DIR):
        if filename.endswith('.json'):
            file_path = os.path.join(PROFILES_DIR, filename)
            try:
                with open(file_path, 'r') as f:
                    profile_data = json.load(f)
                    profiles.append({'filename': filename, 'data': profile_data})
            except json.JSONDecodeError:
                profiles.append({'filename': filename, 'error': 'Invalid JSON'})
    # Sort by profileOrder if available
    preferences = load_preferences()
    profile_order = preferences.get('profileOrder', [])
    if profile_order:
        order_map = {fn: i for i, fn in enumerate(profile_order)}
        profiles.sort(key=lambda x: order_map.get(x['filename'], len(profile_order)))
    return profiles

# Load a single profile by filename
def load_profile(filename):
    file_path = os.path.join(PROFILES_DIR, filename)
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        return json.load(f)

# Save a profile (create or overwrite)
def save_profile(filename, data):
    ensure_profiles_dir()
    file_path = os.path.join(PROFILES_DIR, filename)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

# Delete a profile by filename
def delete_profile(filename):
    file_path = os.path.join(PROFILES_DIR, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        # Remove from profileOrder in preferences
        preferences = load_preferences()
        profile_order = preferences.get('profileOrder', [])
        if filename in profile_order:
            profile_order.remove(filename)
            preferences['profileOrder'] = profile_order
            save_preferences(preferences)
        return True
    return False

# Add a new profile (returns filename)
def add_profile(profile_data):
    ensure_profiles_dir()
    profile_data['created'] = datetime.now().isoformat()
    filename = f"{uuid.uuid4()}.json"
    save_profile(filename, profile_data)
    # Add to profileOrder
    preferences = load_preferences()
    profile_order = preferences.get('profileOrder', [])
    profile_order.append(filename)
    preferences['profileOrder'] = profile_order
    save_preferences(preferences)
    return filename

# Edit an existing profile
def edit_profile(filename, profile_data):
    file_path = os.path.join(PROFILES_DIR, filename)
    if not os.path.exists(file_path):
        return False
    try:
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
            profile_data['created'] = existing_data.get('created')
    except json.JSONDecodeError:
        return False
    save_profile(filename, profile_data)
    return True

# Deactivate all profiles except the given filename
def deactivate_all_except(filename):
    ensure_profiles_dir()
    updated_count = 0
    for profile_filename in os.listdir(PROFILES_DIR):
        if profile_filename.endswith('.json'):
            file_path = os.path.join(PROFILES_DIR, profile_filename)
            try:
                with open(file_path, 'r') as f:
                    profile_data = json.load(f)
                profile_data['isActive'] = (profile_filename == filename)
                with open(file_path, 'w') as f:
                    json.dump(profile_data, f, indent=2)
                updated_count += 1
            except json.JSONDecodeError:
                continue
    return updated_count 