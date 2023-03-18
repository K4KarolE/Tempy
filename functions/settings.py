import json
import os
from pathlib import Path

functions_directory = os.path.dirname(__file__)
main_directory = functions_directory.replace("functions",'')
path_json = Path(main_directory, "json", "settings_db.json")    

def open_settings():
    f = open(path_json)
    settings_data = json.load(f)
    return settings_data

def save_settings(settings_data):
    with open(path_json, 'w') as f:
        json.dump(settings_data, f, indent=2)
    return

# settings_data = open_settings() 
# save_settings(settings_data)