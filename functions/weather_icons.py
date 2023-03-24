'''
- Checks the weather json files and downloads the missing icon images
- Placed/actioned:  settings_window.py / Select button`s command
'''
import urllib.request
import os
from pathlib import Path

from functions import management


def download():
    ## LOAD WEATHER DATA
    current_w_dic = management.load_weather_data("weather_current.json")
    five_day_w_dic = management.load_weather_data("weather_5_days.json")

    ### DOWNLOADING THE MISSING ICONS
    ## ICON LISTS
    icon_list = []
    # CURRENT
    icon = f"{current_w_dic['weather'][0]['icon']}.png"
    icon_list.append(icon)
    # FIVE DAY
    for item in five_day_w_dic['list']:
        icon = f"{item['weather'][0]['icon']}.png"
        if icon not in icon_list:
            icon_list.append(icon)

    path_weather_icons_folder = Path(management.main_directory(), 'docs', 'weather_icons' )
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
