
import sys
import os
from tkinter import *
from pathlib import Path

from datetime import datetime
from datetime import timedelta

from functions import settings
from functions import api
from functions import weather_icons

from functions import settings_window
from functions import image_display
from functions import management

## TEXT
class Text:
    def __init__(self, text, font_style, font_size):
        self.text = text
        self.font_style = font_style
        self.font_size = font_size
    
    def create(self):
        return Label(window,
                     text = self.text,
                     font = (self.font_style, self.font_size, 'bold'),
                     foreground=font_color,
                     background=background_color)


## GET WEATHER DATA - BY STARTING THE APP AUTOMATICALLY GET THE LAST USED CITY`S NEW WEATHER DETAILS
api.get_weather_data()
# DOWNLOAD MISSING WEATHER ICONS
weather_icons.download()
# ACCESS TO SETTINGS_DB.JSON
settings_data = settings.open_settings()   

# COLORS - FONT STYLE
# FYI:
    # original tkinter grey: #F0F0F0
    # office grey: #DEDEDE
window_background_color = settings_data['window_background_color']
background_color = settings_data['background_color'] 
field_background_color = settings_data['field_background_color'] 
font_style = settings_data['font_style']
font_size = settings_data['font_size']
font_color = settings_data['font_color']


## WINDOW
window = Tk()
window.title(settings_data['window_title'])
window_width = settings_data['window_width']
window_length = settings_data['window_original_length']
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width/2-275, screen_height/5))    #   position to the middle of the screen
window.resizable(0,0)   # locks the main window
window.configure(background=settings_data['background_color'])
# WINDOW ICON
if sys.platform != 'linux':
    working_directory = os.path.dirname(__file__)
    path_icon = Path(working_directory, "skin", "icon.ico") 
    window.iconbitmap(path_icon)
# BACKGROUND IMAGE 
main_directory = os.path.dirname(__file__)
path_image = Path(main_directory, "skin", "BG.png")
backgound_image = PhotoImage(file = path_image)
backgound_image_label = Label(window, image = backgound_image, background=window_background_color)
backgound_image_label.place(x = -2, y = 0)

### WIDGETS
## SETTINGS BUTTON
launched = 0
def window_launched_counter(): # CREATING THE SETTINGS WIDOW WIDGETS ONLY ONCE @ FIRST OPENING
    global launched
    launched += 1

photo_cog = image_display.button(24,"icon_cog_popup.png")
settings_button = Button(window,
                      command = lambda: [window_launched_counter(), settings_window.launch(launched, window)],
                      image = photo_cog,
                      foreground=font_color, 
                      background=background_color, 
                      activeforeground=background_color, 
                      activebackground='#505050')
settings_button.place(x=window_width - 50, y=110)



### DISPLAY DATA
## CURRENT WEATHER DATA
current_weather_widget_list = []
# LOAD WEATHER DATA
current_w_dic = management.load_weather_data("weather_current.json")

# CITY NAME
city_name_text = settings_data['city_selected']
city_name_instance = Text(city_name_text, font_style, 18)
city_name = city_name_instance.create()
city_name.place(x=window_width/2-10, y=90, anchor = CENTER)
current_weather_widget_list.append(city_name)

## TEMP / HUM / WIND - FONT SIZE / STYLE
details_font_size = 15
details_font_style = font_style
details_y_base = 120
details_y_gap = 30

# TEMPERATURE
temp_type = settings_data['temp_type_selected'][0]
temp_text = f"{round(current_w_dic['main']['temp'])}\xb0{temp_type}"     # \xb0 = degree sign
temp_instance = Text(temp_text, details_font_style, details_font_size)
temp = temp_instance.create()
temp.place(x=window_width/2, y=details_y_base + details_y_gap * 0, anchor = NW)
current_weather_widget_list.append(temp)

# HUMIDITY
hum_text = f"{current_w_dic['main']['humidity']} %"     # \xb0 = degree sign
hum_instance = Text(hum_text, details_font_style, details_font_size)
hum = hum_instance.create()
hum.place(x=window_width/2, y=details_y_base + details_y_gap * 1, anchor = NW)
current_weather_widget_list.append(hum)

# WIND
if temp_type == 'C':
    wind_type = 'kmph'
else:
    wind_type = 'mph' 
wind_text = f"{round(current_w_dic['wind']['speed'])} {wind_type}"     # \xb0 = degree sign
wind_instance = Text(wind_text, details_font_style , details_font_size)
wind = wind_instance.create()
wind.place(x=window_width/2, y=details_y_base + details_y_gap * 2, anchor = NW)
current_weather_widget_list.append(wind)

# ICON
icon_name = current_w_dic['weather'][0]['icon']
icon_image = image_display.weather_icon(80, icon_name)
icon_image_widget = Label(window, image=icon_image, background=window_background_color)
icon_image_widget.place(x=window_width/2, y=125, anchor = NE)
current_weather_widget_list.append(icon_image_widget)

# SUNRISE
sunrise_timestamp = current_w_dic['sys']['sunrise']
sunrise_dt = datetime.fromtimestamp(sunrise_timestamp)  # 2023-03-28 06:55:41
sunrise = str(sunrise_dt).split(' ')[1][0:5]            # 06:55
sunrise_text = f'Sunrise: {sunrise}'
sunrise_instance = Text(sunrise_text, details_font_style, details_font_size)
sunrise = sunrise_instance.create()
sunrise.place(x=window_width/2+100, y=details_y_base + details_y_gap * 1, anchor = NW)
current_weather_widget_list.append(sunrise)
# SUNSET
sunset_timestamp = current_w_dic['sys']['sunset']
sunset_dt = datetime.fromtimestamp(sunset_timestamp)
sunset = str(sunset_dt).split(' ')[1][0:5]
sunset_text = f'Sunset:   {sunset}'
sunset_instance = Text(sunset_text, details_font_style, details_font_size)
sunset = sunset_instance.create()
sunset.place(x=window_width/2+100, y=details_y_base + details_y_gap * 2, anchor = NW)
current_weather_widget_list.append(sunset)



## 5 DAY WEATHER DATA
# TIMES
time_list = [ '00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
n = 0
time_list_y = 230
for item in time_list:
    time_instance = Text(item, details_font_style , 15)
    time = time_instance.create()
    time.place(x=window_width/5 + n, y=time_list_y)
    n += 75

# DAYS
days_list = ["Today"]   # Today, Sunday, Monday, ..
for i in range(1,6):
    days_list.append((datetime.now()+timedelta(i)).strftime('%A'))

n = 0
for item in days_list:
    days_instance = Text(item, details_font_style , 15)
    days = days_instance.create()
    days.place(x=30, y=time_list_y + 50 + n)
    n += 81

# ICONS - WEATHER DATA
five_days_fcast = management.load_weather_data('weather_5_days.json')
# DELAY CALC
five_days_fcast_first_datetime = five_days_fcast['list'][0]['dt']   # app triggered at 20:00->only the 21:00 data will be displayed
todays_first_datetime = management.todays_first_datetime()
delay = int((five_days_fcast_first_datetime - todays_first_datetime)/10800)
# DISPLAY
if delay < 8:
    x_counter = 1 + delay # only available data will be displayed at the correct time spot
    y_counter = 0
    
else:               # after 21:00, the next day 00:00AM will be the first -> TODAY row will be empty
    x_counter = 1
    y_counter = 1

x_gap = 75    
y_gap = 80
five_day_icon_image = []            # to avoid garbage collection
five_day_icon_image_widget = []     # to avoid garbage collection
five_day_w_data_widget = []
n=0
for item in five_days_fcast['list']:
    # WEATHER ICONS
    five_day_icon_name = item['weather'][0]['icon']
    five_day_icon_image.append(image_display.weather_icon(60, five_day_icon_name))
    five_day_icon_image_widget.append(Label(window, image=five_day_icon_image[n], background=background_color))
    five_day_icon_image_widget[n].place(x= window_width/5 - x_gap + x_counter * x_gap - 5, y=time_list_y + 30 + y_counter * y_gap)
    
    # WEATHER DATA
    five_day_w_data_font_size = 11
    five_day_w_data_widget_instance = []
    temp_five_day = round(item['main']['temp'])
    hum_five_day = item['main']['humidity']
    five_day_w_data = f'{temp_five_day}\xb0 {hum_five_day}%'
    five_day_w_data_widget.append(Text(five_day_w_data, details_font_style, five_day_w_data_font_size).create())
    five_day_w_data_widget[n].place(x= window_width/5 - x_gap + x_counter * x_gap + 25, y=time_list_y + 90 + y_counter * y_gap, anchor=CENTER)
    
    n += 1
    if x_counter % 8 == 0:
        x_counter = 0
        y_counter += 1
    x_counter += 1

# REMOVE PREVIOUS WIDGETS
# def remove_previous_widgets():
#     ## CURRENT WEATHER DATA
#     for item in current_weather_widget_list:
#         item.destroy()
#     ## 5 DAY WEATHER DATA
#     # ICONS
#     for item in five_day_icon_image_widget:
#         item.destroy()
#     # TEXT
#     for item in five_day_w_data_widget:
#         item.destroy()

# remove_button = Button(window,
#                       command = lambda: [remove_previous_widgets()],
#                       text="Remove",
#                       height = 1,
#                       width = 6,
#                       foreground=font_color, 
#                       background=background_color, 
#                       activeforeground=background_color, 
#                       activebackground='#505050')
# remove_button.place(x=window_width - 70, y=150)


     
window.mainloop()
