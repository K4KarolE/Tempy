
import os
from tkinter import *
from pathlib import Path

# from functions import messages
from functions import settings
from functions import settings_window
from functions import image_display
from functions import management


# ACCESS TO SETTINGS_DB.JSON
settings_data = settings.open_settings()   

# COLORS - FONT STYLE
# original tkinter grey: #F0F0F0 - FYI
background_color = settings_data['background_color'] 
field_background_color = settings_data['field_background_color'] 
font_style = settings_data['font_style']
font_size = settings_data['font_size']
font_color = settings_data['font_color']


# WINDOW
window = Tk()
window.title(settings_data['window_title'])
window_width = 550
window_length = 445
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width/2-275, screen_height/2-125))    #   position to the middle of the screen
window.resizable(0,0)   # locks the main window
window.configure(background=settings_data['background_color'])
# ICON
working_directory = os.path.dirname(__file__)
path_icon = Path(working_directory, "skin", "icon.ico") 
window.iconbitmap(path_icon)
# RECTANGLE
canvas_color = settings_data['background_color']
canvas_frame_color = settings_data['canvas_frame_color']
canvas = Canvas(window, width=window_width, height=window_length, background = background_color)
canvas.create_rectangle(5-1, 5+2, window_width-5, window_length-5, outline=canvas_frame_color, fill=canvas_color)
canvas.pack()


## WIDGETS
# SETTINGS BUTTON
photo_cog = image_display.button(24,"icon_cog_popup.ico")
settings_button = Button(window,
                      command = lambda: [settings_window.launch(window, canvas)],
                      image = photo_cog, 
                      height = 30,
                      width = 30,
                      foreground=font_color, 
                      background=background_color, 
                      activeforeground=background_color, 
                      activebackground='#505050')

## TEXT, ICONS
class Text:
    def __init__(self, text, font_style, font_size):
        self.text = text
        self.font_style = font_style
        self.font_size = font_size
    
    def create(self):
        return Label(window,
                     text = self.text,
                     font = (self.font_style, self.font_size),
                     foreground=font_color,
                     background=background_color)

## CURRENT WEATHER DATA
##LOAD WEATHER DATA
current_w_dic = management.load_weather_data("weather_current.json")
# CITY NAME
city_name_instance = Text(settings_data['city_selected'],'Georgia', 18)
city_name = city_name_instance.create()
city_name.place(x=200, y=30)
# TEMP / HUM / WIND - FONT SIZE / STYLE
details_font_size = 15
details_font_style = 'Arial'
# TEMPERATURE
temp_text = f"{current_w_dic['main']['temp']} \xb0"     # \xb0 = degree sign
temp_instance = Text(temp_text, details_font_style, details_font_size)
temp = temp_instance.create()
temp.place(x=280, y=80)
# HUMIDITY
hum_text = f"{current_w_dic['main']['humidity'] }%"     # \xb0 = degree sign
hum_instance = Text(hum_text, details_font_style, details_font_size)
hum = hum_instance.create()
hum.place(x=310, y=120)
# WIND
wind_text = f"{current_w_dic['wind']['speed']} W"     # \xb0 = degree sign
wind_instance = Text(wind_text, details_font_style , details_font_size)
wind = wind_instance.create()
wind.place(x=310, y=160)
# ICON
icon_name = current_w_dic['weather'][0]['icon']
icon_image = image_display.weather_icon(100, icon_name)
icon_image_widget = Label(window, image=icon_image, background=canvas_color)
icon_image_widget.place(x=150, y=90)
# class Icon:  
#     def __init__(self, size):
#         self.size = size
    
#     def create(self):
#         return Text(window, 
#                     height = 1, 
#                     width = self.width, 
#                     foreground=font_color, 
#                     background=self.background, 
#                     font=(font_style, font_size))


  

### DISPLAY WIDGETS
def display_widgets():
    # BASE VALUES
    # FIELD
    # x_field = 17
    # y_field = 20
    # # BUTTON
    # x_button = 350
    # y_button_base = 15
    # y_diff_from_start = 15

    # def y_button(gap):
    #     location = y_button_base + 23 * gap
    #     return location
        
    # SETTINGS BUTTON
    settings_button.place(x=window_width - 50, y=20)


    # THUMBNAIL
    # thumbnail.place(x=thumbnail_x, y=thumbnail_y)


display_widgets()


window.mainloop()
