# SETTINGS COG BUTTON

from tkinter import *

import os
from pathlib import Path

# from functions import messages
from functions import settings
# import settings
settings_data = settings.open_settings()

from functions import api
# import api


def launch(window, canvas):

    # SEARCH FIELD LENGTH
    search_field_length = 22
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
    window_width =  550    
    window_length = 650    
    window.geometry(f'{window_width}x{window_length}')
    
    # RESIZE CANVAS - AADD NEW FRAME/RECTANGLE
    canvas_color = settings_data['background_color']
    canvas_frame_color = settings_data['canvas_frame_color']
    canvas.configure(width=window_width, height=window_length, bg=background_color)
    canvas.create_rectangle(5-1, 445, window_width-5, window_length-5, outline=canvas_frame_color, fill=canvas_color)

    # CLASSES
    class Buttons:
        def __init__(self, text, command):
            self.text = text
            self.command = command
        
        def create(self):
            return Button(window, 
                            height=button_height,
                            width=button_width,
                            text = self.text,
                            command = self.command,
                            foreground=font_color,
                            background=background_color,
                            activeforeground=background_color,
                            activebackground=font_color,
                            font=(font_style, font_size))
        # CELSIUS - FAHRENHEIT
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
            return Text(window,
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
        city_select_roll_down = OptionMenu( window, city_select_roll_down_clicked, *city_select_list, command=None)
        city_select_roll_down.configure(font=(font_style, font_size), foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
        city_select_roll_down['menu'].configure(font=(font_style, font_size), foreground=font_color, background=background_color, activebackground='grey')
        city_select_roll_down.place(x=25, y=y_location(4))   

    city_search_button_instance = Buttons("Search", lambda:[city_search()])
    city_search_button = city_search_button_instance.create()


    ## CITY SELECT - ROLL DOWN MENU + BUTTON
    # ROLL DOWN MENU
    city_select_list=["None"]
    city_select_roll_down_clicked = StringVar()
    city_select_roll_down_clicked.set("  Search for the city first ")
    city_select_roll_down = OptionMenu( window, city_select_roll_down_clicked, *city_select_list, command=None)     
    city_select_roll_down.configure(font=(font_style, font_size), foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
    city_select_roll_down['menu'].configure(font=(font_style, font_size), foreground=font_color, background=background_color, activebackground='grey')

    # BUTTON
    # CITY SELECTED - ACTIONS
    def city_selected():
        #SAVE SELECTED CITY
        city_selected = city_select_roll_down_clicked.get()
        settings_data = settings.open_settings()
        settings_data['city_selected'] = city_selected
        # settings_data['city_selected_name'] = city_selected.split(',')[0] - it is in weather_current.json
        settings.save_settings(settings_data)
        # GET WEATHER DATA
        api.get_weather_data()

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
    y_button_base = 500

    def y_location(gap):
        location = y_button_base + 20 * gap
        return location

    # SAVE BUTTON
    celsius_button.place(x=25, y=y_location(0))

    # SAVE BUTTON
    fahrenheit_button.place(x=125, y=y_location(0))


    # SEARCH CITY - FIELD + BUTTON
    city_search_field.place(x=25, y=y_location(1)+20)
    city_search_button.place(x=x_button, y=y_location(1)+20)

    # SELECT CITY - FIELD + BUTTON
    city_select_roll_down.place(x=25, y=y_location(4))
    city_select_button.place(x=x_button, y=y_location(4))

    window.mainloop()

