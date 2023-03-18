'''
- add city name -> geo API -> if there is more than one, list them (max 5 be default) with country, states(just US)
- able to select from which country, states -> get coordinates
- GET current temp.
- GET 5 day forecast (icons?, day/3 hours data -> graphs?, display lowest, max temp. before and after graph? // graph with Pandas?)
- display results, save city details as last call
- next app open: automatically starts(calls the API) with the last city by default
'''

import requests
import json
import os
from pathlib import Path

# from functions import messages
# from functions import settings
import settings


functions_directory = os.path.dirname(__file__)     # = D:\_DEV\Python\MODDEC\functions   //in my case
main_directory = functions_directory.replace("functions",'')

def path_json(name_json):
    path_json = Path(main_directory,  "json", name_json)
    return path_json   


# API KEY
path_api_key = Path(main_directory, 'api_key.txt')
file = open(path_api_key)
api_key = file.read()
file.close()


def find_city():
    settings_data = settings.open_settings()
    city = settings_data['city_added']
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



## FIVE DAY / 3 HOUR FORECAST
def get_five_day():
    settings_data = settings.open_settings()
    city_selected= settings_data['city_selected']
    lat = settings_data['city_list'][city_selected]['lat']
    lon = settings_data['city_list'][city_selected]['lon']
    temp_type_selected = settings_data['temp_type_selected']    # example: Celsius
    temp_type = settings_data['temp_type'][temp_type_selected]  # example: metric

    link_five_day = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={temp_type}&appid={api_key}'
    response = requests.get(link_five_day)

    # SAVE, LOAD 'FIVE DAY FORECAST' RESPONSE
    with open(path_json('5_day_forecast.json'), 'w') as f:
        json.dump(response.json(), f, indent=2)


# find_city()
# get_five_day()


