import os
import json

# Path to the preferences file
PREFERENCES_FILE = 'data/user_preferences.json'

def load_preferences():
    '''Load user preferences from file'''
    if os.path.exists(PREFERENCES_FILE):
        try:
            with open(PREFERENCES_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return get_default_preferences()
    return get_default_preferences()

def save_preferences(preferences):
    '''Save user preferences to file'''
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(PREFERENCES_FILE), exist_ok=True)
    
    with open(PREFERENCES_FILE, 'w') as f:
        json.dump(preferences, f, indent=2)

def get_default_preferences():
    '''Get default preferences structure'''
    return {
        'profileOrder': []
    }

def update_profile_order(profile_order):
    '''Update the profile order in preferences'''
    preferences = load_preferences()
    preferences['profileOrder'] = profile_order
    save_preferences(preferences)
    return preferences 