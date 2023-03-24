
import requests
import json
import os
from pathlib import Path

# from functions import messages
from functions import settings
from functions import management


# API KEY
path_api_key = Path(management.main_directory(), 'api_key.txt')
file = open(path_api_key)
api_key = file.read()
file.close()


def find_city(city):
    settings_data = settings.open_settings()
    limit = 5
    link_find_city = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={api_key}'
    response = requests.get(link_find_city)

    find_city_dic = response.json()

    city_list = {}
    for i in find_city_dic:
        if i['country'] != 'US':
            location_name = f"{i['name']}, {i['country']}"
            city_list[location_name] = {'lat':i["lat"], 'lon':i["lon"]}
        else:
            location_name = f"{i['name']}, {i['country']}, {i['state']}"
            city_list[location_name] = {'lat':i["lat"], 'lon':i["lon"]}

    settings_data['city_list'] = city_list
    settings.save_settings(settings_data)

    # for i in city_list:
    #     print(f'{i}: {city_list[i]["lat"]}, {city_list[i]["lon"]}')
        # Chelsea, GB, England: 51.4875167, -0.1687007



## GET WEATHER DATA
def get_weather_data():
    settings_data = settings.open_settings()
    city_selected= settings_data['city_selected']
    lat = settings_data['city_list'][city_selected]['lat']
    lon = settings_data['city_list'][city_selected]['lon']
    temp_type_selected = settings_data['temp_type_selected']    # example: Celsius
    temp_type = settings_data['temp_type'][temp_type_selected]  # example: metric

    def weather_current():
        link_current = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={temp_type}&appid={api_key}'
        response_link_current = requests.get(link_current)

        with open(management.path_json('weather_current.json'), 'w') as f:
            json.dump(response_link_current.json(), f, indent=2)
    
    def weather_5_day():
        link_five_day = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={temp_type}&appid={api_key}'
        response_link_five_day = requests.get(link_five_day)
        
        with open(management.path_json('weather_5_days.json'), 'w') as f:
            json.dump(response_link_five_day.json(), f, indent=2)
        
    weather_current()
    weather_5_day()