import glob
import shutil
import os
from PIL import Image
import tkinter
from tkinter import filedialog as fd 

curr_directory = os.getcwd() # will get current working directory
name = fd.askopenfilename(initialdir = curr_directory,title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
dir_path = r"C/Users/PP/Desktop/Minor Project 2nd SEM/input_img"
for filename in os.listdir(name):
    img = Image.open(os.path.join(name, filename)) # images are color images
    img = img.resize((224,224), Image.ANTIALIAS)
    img.save(dir_path+filename+'.jpeg') 