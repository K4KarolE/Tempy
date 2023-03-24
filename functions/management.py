import json
import os
from pathlib import Path


def main_directory():
    functions_directory = os.path.dirname(__file__)  
    directory = functions_directory.replace("functions",'')
    return directory


def path_json(name_json):
    path_json = Path(main_directory(), "json", name_json)
    return path_json


def load_weather_data(weather_json):
    f = open(path_json(weather_json))
    weather_dictionary = json.load(f)
    return weather_dictionary




