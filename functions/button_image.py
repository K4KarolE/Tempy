from PIL import Image
from PIL import ImageTk
from pathlib import Path
import os

def create(image_size, picture_name):       # (24, "icon_close.png")
    functions_directory = os.path.dirname(__file__)
    main_directory = functions_directory.replace("functions",'')
    my_img_path = Path(main_directory, "skin", picture_name)
    my_img = Image.open(my_img_path)
    width = int(image_size)
    height = int(image_size)
    resized_image = my_img.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo