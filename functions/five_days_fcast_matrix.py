'''
A,
Creating a dictionary where the keys named with integer values of
date of the day @ 00:00:00 -> 1679529600
date of the day @ 00:03:00
..
*48 -> covers the today - +5 days range

B,
allocating the current available weather data to the matching int date
'''

from datetime import datetime
from datetime import date

import json
import os
from pathlib import Path


# TIMESTAMPS AND '5 DAYS FORECAST MATRIX' CREATION
today_date = date.today()
today_datetime_zero = datetime.strptime(str(today_date), '%Y-%m-%d') # 2023-03-23 00:00:00
datetime_int  = int(today_datetime_zero.timestamp())    # 1679529600

five_day_fcast_matrix = {}
counter = 0
while counter < 48: # day/3hrs * 6 (5 day forcast from the current time -> overlaping, the first and last day: no full forecast)
    five_day_fcast_matrix[datetime_int + 10800 * counter] = {}   # 10800 = 3hrs jump / 2023-03-23 00:00:00 -> 2023-03-23 00:03:00
    counter += 1

# INT DATETIME CHECK
# print(five_day_dic)
# import datetime
# for i in five_day_dic:
#     print(datetime.datetime.fromtimestamp(i))


# '5 DAYS FORECAST MATRIX' VALUE ALLOCATION
functions_directory = os.path.dirname(__file__)
main_directory = functions_directory.replace("functions",'')

def path_json(name_json):
    path_json = Path(main_directory, "json", name_json)
    return path_json   

f = open(path_json('weather_5_days.json'))
weather_5_day_json = json.load(f)

for item in weather_5_day_json['list']:
    date_int = item['dt']
    five_day_fcast_matrix[date_int] = item

with open(path_json('weather_5_days_matrix.json'), 'w') as f:
            json.dump(five_day_fcast_matrix, f, indent=2)