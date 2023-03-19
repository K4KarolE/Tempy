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
window_width = 447
window_length = 138
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
yt_dlp_location_field_instance = Fields(search_field_length, "white")
yt_dlp_location_field = yt_dlp_location_field_instance.create()


def browse_location_yt_dlp():
    file_name = filedialog.askopenfilename(initialdir = "/",
                title = "Select a File",
                filetypes = (("Executable", "*.exe"),
                            ("all files", "*.*")))
    yt_dlp_location_field.delete('1.0', END)       # once a button is clicked, removes the previous value
    yt_dlp_location_field.insert(END,file_name)     # adding the path and the name of the selected file

yt_dlp_location_button_instance = Buttons("Search", lambda:[browse_location_yt_dlp()])
yt_dlp_location_button = yt_dlp_location_button_instance.create()


## SELECT CITY - FIELD + BUTTON
ffmpeg_location_field_instance = Fields(search_field_length,"white")
ffmpeg_location_field = ffmpeg_location_field_instance.create()


def browse_location_ffmpeg():
    file_name = filedialog.askopenfilename(initialdir = "/",
                title = "Select a File",
                filetypes = (("Executable", "*.exe"),
                            ("all files", "*.*")))
    ffmpeg_location_field.delete('1.0', END)       # once a button is clicked, removes the previous value
    ffmpeg_location_field.insert(END,file_name)     # adding the path and the name of the selected file

ffmpeg_location_button_instance = Buttons("Select", lambda: [browse_location_ffmpeg()])
ffmpeg_location_button = ffmpeg_location_button_instance.create()


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
yt_dlp_location_field.place(x=25, y=70)
yt_dlp_location_button.place(x=x_button, y=y_location(0)+2)

# SELECT CITY - FIELD + BUTTON
ffmpeg_location_field.place(x=25, y=100)
ffmpeg_location_button.place(x=x_button, y=y_location(2)-2)

top_window.mainloop()


