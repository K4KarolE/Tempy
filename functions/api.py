
import requests
import json
from pathlib import Path

from functions import messages
from functions import settings
from functions import management


# API KEY
# OpenWeather API - Plan Free: 60 calls/minute - 1,000,000 calls/month
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
    
    if len(find_city_dic) != 0:
        city_list = {}
        for i in find_city_dic:
            if i['country'] != 'US':
                location_name = f"{i['name']}, {i['country']}"
                city_list[location_name] = {'lat':i["lat"], 'lon':i["lon"]}
            else:
                location_name = f"{i['name']}, {i['country']}, {i['state']}"
                city_list[location_name] = {'lat':i["lat"], 'lon':i["lon"]}

        settings_data['city_list'] = city_list
        settings_data['city_search_valid'] = "True"
        settings.save_settings(settings_data)
    else:
        settings_data['city_search_valid'] = "False"
        settings.save_settings(settings_data)
        messages.error_pop_up('Error','invalid_city_name')


## GET WEATHER DATA
def get_weather_data():
    settings_data = settings.open_settings()
    city_selected= settings_data['city_selected']
    try: 
        lat = settings_data['city_list'][city_selected]['lat']
        lon = settings_data['city_list'][city_selected]['lon']
        temp_type_selected = settings_data['temp_type_selected']    # example: Celsius
        temp_type = settings_data['temp_type'][temp_type_selected]  # example: metric

        def weather_current():
            link_current = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={temp_type}&appid={api_key}'
            response_link_current = requests.get(link_current)

            if len(response_link_current.json()) != 0:
                with open(management.path_json('weather_current.json'), 'w') as f:
                    json.dump(response_link_current.json(), f, indent=2)
            else:
                messages.error_pop_up('Error','api_weather_current')
        
        def weather_5_day():
            link_five_day = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={temp_type}&appid={api_key}'
            response_link_five_day = requests.get(link_five_day)
            
            if len(response_link_five_day.json()) != 0:
                with open(management.path_json('weather_5_days.json'), 'w') as f:
                    json.dump(response_link_five_day.json(), f, indent=2)
            else:
                messages.error_pop_up('Error','api_weather_5_day')
            
        weather_current()
        weather_5_day()
    except:
        messages.error_pop_up('Error','no_latitude_longitude')