import urllib.request
import json
import os
from pathlib import Path


# LOAD WEATHER DATA
functions_directory = os.path.dirname(__file__)  
main_directory = functions_directory.replace("functions",'')

def path_json(name_json):
    path_json = Path(main_directory,  "json", name_json)
    return path_json

f = open(path_json('weather_current.json'))
current_dic = json.load(f)

f = open(path_json('weather_5_day.json'))
five_day_dic = json.load(f)


### DOWNLOADING THE MISSING ICONS
## ICON LISTS
icon_list = []
# CURRENT
icon = f"{current_dic['weather'][0]['icon']}.png"
icon_list.append(icon)
# FIVE DAY
for item in five_day_dic['list']:
    icon = f"{item['weather'][0]['icon']}.png"
    if icon not in icon_list:
        icon_list.append(icon)
path_weather_icons_folder = Path(main_directory, 'docs', 'weather_icons' )
icon_already_existing = os.listdir(path_weather_icons_folder)

# MISSING ICONS
icon_missing =[]
for item in icon_list:
    if item not in icon_already_existing:
        icon_missing.append(item)

## DOWNLOAD ICON
if len(icon_missing) != 0:
    for icon in icon_missing:
        try:
            url = f'https://openweathermap.org/img/w/{icon}'
            urllib.request.urlretrieve(url, Path(path_weather_icons_folder, icon))
        except:
            print(f'Failed to download the {icon} icon.')
