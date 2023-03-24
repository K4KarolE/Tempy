from PIL import Image
from PIL import ImageTk
from pathlib import Path

from functions import management


main_directory = management.main_directory()

def button(image_size, picture_name):       # (24, "icon_close.png")
    my_img_path = Path(main_directory, "skin", picture_name)
    my_img = Image.open(my_img_path)
    width = int(image_size)
    height = int(image_size)
    resized_image = my_img.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo

def weather_icon(image_size, icon_name):       # (24, "01d")
    my_img_path = Path(main_directory, "docs", "weather_icons" , icon_name, ".png")
    my_img = Image.open(my_img_path)
    width = int(image_size)
    height = int(image_size)
    resized_image = my_img.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo