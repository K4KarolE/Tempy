
import os

from tkinter import *

from PIL import Image               # PILLOW import has to be after the tkinter impoert (Image.open will not work: 'Image has no attributesm open')
from PIL import ImageTk

from pathlib import Path

# from functions import messages
from functions import settings
settings_data = settings.open_settings()        # access to the saved/default settings (settings_db.json)

from functions import settings_window


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
## SETTINGS BUTTON - POP UP WINDOW
my_img_path = Path(working_directory, "skin", "icon_cog_popup.ico")
my_img = Image.open(my_img_path)
width = int(24)
height = int(24)
resized_image = my_img.resize((width, height))
# global img  # otherwise it will not be displayed - Garbage Collection - https://stackoverflow.com/questions/16424091/why-does-tkinter-image-not-show-up-if-created-in-a-function
photo_cog = ImageTk.PhotoImage(resized_image)

settings_button = Button(window,
                      command = lambda: [settings_window.launch(window, canvas)],
                      image = photo_cog, 
                      height = 30,
                      width = 30,
                      foreground=font_color, 
                      background=background_color, 
                      activeforeground=background_color, 
                      activebackground='#505050')

## GET URL - BUTTON
# REMOVE PREVIOUS VALUES - THUMBNAIL
# DISPLAY THUMBNAIL
# path_thumbnail_default = Path(working_directory, "thumbnail", "thumbnail_default.png") 
# my_img = Image.open(path_thumbnail_default)
# img = ImageTk.PhotoImage(my_img)
# thumbnail = Label(window, image=img, background=canvas_color)
# thumbnail_x = settings_data['thumbnail_location_x']
# thumbnail_y = settings_data['thumbnail_location_y']

    

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
