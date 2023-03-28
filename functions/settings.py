import json
from functions import management

path_settings_json = management.path_json("settings_db.json")   

def open_settings():
    f = open(path_settings_json)
    settings_data = json.load(f)
    return settings_data

def save_settings(settings_data):
    with open(path_settings_json, 'w') as f:
        json.dump(settings_data, f, indent=2)
    return

# settings_data = open_settings() 
# save_settings(settings_data)