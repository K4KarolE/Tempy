# SETTINGS BUTTON - POP UP WINDOW

from tkinter import *
from tkinter import filedialog

import webbrowser
import os
from pathlib import Path

# from functions import messages
# from functions import settings
import settings
settings_data = settings.open_settings()

# from functions import api
import api


# SEARCH FIELD LENGTH
search_field_length = 22

# def launch(window):
settings_data = settings.open_settings()

# COLORS - FONT STYLE
background_color = settings_data['background_color']
font_style = settings_data['font_style']
font_size = settings_data['font_size']
font_color = settings_data['font_color']

# BUTTON SIZE
button_height = 1
button_width = 10
# WINDOW     
top_window = Tk() #Toplevel()
top_window.title("Settings")
window_width =  447    #447
window_length = 200    #138
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
# top_window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width/2+180, screen_height/2+27))    
top_window.resizable(0,0)
top_window.configure(background=settings_data['background_color'])
# ICON
working_directory = os.path.dirname(__file__).strip('functions')
path_icon_popup = Path(working_directory, "skin", "icon_popup.ico") 
top_window.iconbitmap(path_icon_popup)
# RECTANGLES
canvas_color = settings_data['background_color']
canvas_frame_color = settings_data['canvas_frame_color']
canvas = Canvas(top_window, width=window_width, height=window_length, background = background_color)
canvas.create_rectangle(5-1, 5+2, window_width-5, window_length-5, outline=canvas_frame_color, fill=canvas_color)
canvas.pack()

# CLASSES
class Buttons:
    def __init__(self, text, command):
        self.text = text
        self.command = command
    
    def create(self):
        return Button(top_window, 
                        height=button_height,
                        width=button_width,
                        text = self.text,
                        command = self.command,
                        foreground=font_color,
                        background=background_color,
                        activeforeground=background_color,
                        activebackground=font_color,
                        font=(font_style, font_size))
    
    def selected(self):
        return self.configure(foreground=background_color,
                         background="#505050",
                         activeforeground=background_color,
                         activebackground=background_color)
    
    def standard(self):
        return self.configure(foreground=font_color,
                        background=background_color,
                        activeforeground=background_color,
                        activebackground=font_color)

class Fields:
    def __init__(self, width, background):
        self.width = width
        self.background = background
    
    def create(self):
        return Text(top_window,
                    height = 1,
                    width = self.width,
                    foreground=font_color,
                    background=self.background,
                    font=(font_style, "14"))


## WIDGETS
## CITY SEARCH - FIELD + BUTTON
city_search_field_instance = Fields(search_field_length, "white")
city_search_field = city_search_field_instance.create()


def city_search():
    ## CITY SEARCH
    city = city_search_field.get("1.0", "end-1c")
    api.find_city(city)

    ## CITY SELECT
    # CREATE LIST
    settings_data = settings.open_settings()
    city_select_list = []
    for item in settings_data['city_list']:
        city_select_list.append(item)
    city_select_list.sort()
    # DISPLAY THE NEW ROLL DOWN MENU  
    city_select_roll_down_clicked.set(city_select_list[0]) 
    city_select_roll_down = OptionMenu( top_window, city_select_roll_down_clicked, *city_select_list, command=None)
    city_select_roll_down.configure(font=(font_style, font_size), foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
    city_select_roll_down['menu'].configure(font=(font_style, font_size), foreground=font_color, background=background_color, activebackground='grey')
    city_select_roll_down.place(x=25, y=100)   

city_search_button_instance = Buttons("Search", lambda:[city_search()])
city_search_button = city_search_button_instance.create()


## CITY SELECT - ROLL DOWN MENU + BUTTON
# ROLL DOWN MENU
city_select_list=["None"]
city_select_roll_down_clicked = StringVar()
city_select_roll_down_clicked.set("  Search for the city first ")
city_select_roll_down = OptionMenu( top_window, city_select_roll_down_clicked, *city_select_list, command=None)     
city_select_roll_down.configure(font=(font_style, font_size), foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
city_select_roll_down['menu'].configure(font=(font_style, font_size), foreground=font_color, background=background_color, activebackground='grey')

# BUTTON
# CITY SELECTED - ACTIONS
def city_selected():
    city_selected = city_select_roll_down_clicked.get()
    settings_data = settings.open_settings()
    settings_data['city_selected'] = city_selected
    settings_data['city_selected_name'] = city_selected.split(',')[0]
    settings.save_settings(settings_data)

city_select_button_instance = Buttons("Select", lambda: [city_selected()])
city_select_button = city_select_button_instance.create()


## CELSIUS - BUTTON
def celsius():
    # SAVE
    settings_data = settings.open_settings()
    settings_data['temp_type_selected'] = "Celsius"
    settings.save_settings(settings_data)
    # UPDATE COLOR
    Buttons.selected(celsius_button)
    Buttons.standard(fahrenheit_button)
    
celsius_button_instance = Buttons("Celsius", lambda: [celsius()])
celsius_button = celsius_button_instance.create()
if settings_data['temp_type_selected'] == "Celsius":
    Buttons.selected(celsius_button)
   

## FAHRENHEIT - BUTTON
def fahrenheit():
    #SAVE
    settings_data = settings.open_settings()
    settings_data['temp_type_selected'] = "Fahrenheit"
    settings.save_settings(settings_data)
    # UPDATE COLOR
    Buttons.selected(fahrenheit_button)
    Buttons.standard(celsius_button)
           
fahrenheit_button_instance = Buttons("Fahrenheit", lambda: [fahrenheit()])
fahrenheit_button = fahrenheit_button_instance.create()
if settings_data['temp_type_selected'] == "Fahrenheit":
    Buttons.selected(fahrenheit_button)


## DISPLAY WIDGETS
# FIELD
x_field = 17
y_field = 20
# BUTTON
x_button = 300
y_button_base = 25

def y_location(gap):
    location = y_button_base + 20 * gap
    return location

# SAVE BUTTON
celsius_button.place(x=25, y=y_location(0))

# SAVE BUTTON
fahrenheit_button.place(x=125, y=y_location(0))


# SEARCH CITY - FIELD + BUTTON
city_search_field.place(x=25, y=70)
city_search_button.place(x=x_button, y=y_location(1)+20)

# SELECT CITY - FIELD + BUTTON
city_select_roll_down.place(x=25, y=100)
city_select_button.place(x=x_button, y=y_location(3)+18)

top_window.mainloop()


