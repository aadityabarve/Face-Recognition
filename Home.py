from tkinter import *
import tkinter as tk
from PIL import ImageTk,ImageDraw, Image
root = Tk()
f = ("Times bold", 14)
root.title("SMART SPECTACLE")
# open image file
bg = ImageTk.PhotoImage(file="Spec_img2.jpg")
# create canvas
canvas = Canvas(root, width=1000, height=667)
canvas.pack(fill=BOTH, expand=True)
# place the image inside canvas
canvas.create_image(0, 0, image=bg, anchor='nw')
# resize function for resizing the image
# with proper width and height of root window
canvas.create_text(500,100,fill="black",font="Arial 30 bold",
                        text="SMART SPECTACLE",anchor='center')

def nextPage():
    root.destroy()
    import Video_b_rec

def prevPage():
    root.destroy()
    import Image_b_rec

Button(
    root,
    text="Image Based Recognition",
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root,
    text="Video Based Recognition",
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
root.mainloop()