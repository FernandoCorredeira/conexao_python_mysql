from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk



app_img = Image.open('telas/car_logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(image= (app_img))
