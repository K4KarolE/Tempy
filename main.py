
import os
from tkinter import *
from pathlib import Path

# from functions import messages
from functions import settings
from functions import settings_window
from functions import image_display


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

# SEARCH FIELD LENGTH
search_field_length = 40


# class Buttons:
#     def __init__(self, text, command):
#         self.text = text
#         self.command = command
    
#     def create(self):
#         return Button(window,
#                       height=button_height,
#                       width=button_width, text = self.text, 
#                       command = self.command, 
#                       foreground=font_color, 
#                       background=background_color, 
#                       activeforeground=background_color, 
#                       activebackground=font_color)


# class Fields:  
#     def __init__(self, width, background):
#         self.width = width
#         self.background = background
    
#     def create(self):
#         return Text(window, 
#                     height = 1, 
#                     width = self.width, 
#                     foreground=font_color, 
#                     background=self.background, 
#                     font=(font_style, font_size))



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

## CURRENT WEATHER DATA


  

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
