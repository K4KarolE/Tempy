import json
import os
from pathlib import Path
from datetime import datetime
from datetime import date


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


def todays_first_datetime():
    today_date = date.today()
    today_datetime_zero = datetime.strptime(str(today_date), '%Y-%m-%d') # 2023-03-23 00:00:00
    datetime_int  = int(today_datetime_zero.timestamp())    # 1679529600
    return datetime_int
