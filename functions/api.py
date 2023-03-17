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


settings_data = settings.open_settings()

# API KEY
path_api_key = Path(main_directory, 'api_key.txt')
file = open(path_api_key)
api_key = file.read()
file.close()


## FIND CITY
city = "Chelsea"
limit = 5
link_find_city = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={api_key}'
response = requests.get(link_find_city)

# SAVE, LOAD 'FIND CITY' RESPONSE
with open(path_json('find_city.json'), 'w') as f:
    json.dump(response.json(), f, indent=2)

f = open(path_json('find_city.json'))
find_city_dic = json.load(f)

# CITY LIST
list_city_dic = {}
for i in find_city_dic:
    location_name = f"{i['name']}, {i['country']}, {i['state']}"
    list_city_dic[location_name] = {'lat':i["lat"], 'lon':i["lon"]}

# for i in list_city_dic:
#     print(f'{i}: {list_city_dic[i]["lat"]}, {list_city_dic[i]["lon"]}')
    # Chelsea, GB, England: 51.4875167, -0.1687007



## FIVE DAY / 3 HOUR FORECAST
lat = list_city_dic["Chelsea, GB, England"]["lat"]  # will come as chosen one from the city list / UI
lon = list_city_dic["Chelsea, GB, England"]["lon"]

link_five_day = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
response = requests.get(link_five_day)

# SAVE, LOAD 'FIVE DAY FORECAST' RESPONSE
with open(path_json('5_day_forecast.json'), 'w') as f:
    json.dump(response.json(), f, indent=2)

