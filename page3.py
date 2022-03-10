
from tkinter import *
import tkinter as tk
from PIL import ImageTk,ImageDraw, Image
root = Tk()
root.geometry("1000x667")
f = ("Times bold", 14)
root.title("Face Recognised")
# open image file
bg1 = Image.open("Images/Aaditya Barve.jpg")
bg1 = bg1.resize((450,350),Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg1)
# create canvas
canvas = Canvas(root, width=500, height=333)
canvas.pack(fill=BOTH, expand=True)
# place the image inside canvas
canvas.create_image(500, 333, image=bg, anchor='center')
# resize function for resizing the image
# with proper width and height of root window
canvas.create_text(500,90,fill="green",font="Arial 20 bold",
                        text="Successfully Recognised!!! :)",anchor='center')

address_label1=Label(root, text="Address: ",font=("Arial Bold", 8))
address_label2=Label(root, text="I-104,Ganeesham Phase 2,Pimple Saudaghar,Pune,Maharastra.",font=("Arial Bold", 8))
occupation_label1=Label(root, text="Occupation: ",font=("Arial Bold", 8))
occupation_label2=Label(root, text="College Student",font=("Arial Bold", 8))
criminal_record_label1=Label(root, text="Criminal Record: ",font=("Arial Bold", 8))
criminal_record_label2=Label(root, text="No previous criminal record",font=("Arial Bold",8))
description_label1=Label(root, text="Description: ",font=("Arial Bold", 8))
description_label2=Label(root, text="Aaditya Barve is a college student in second year currently studing at MIT Academy of Engineering,Pune",font=("Arial Bold", 8))
address_label1.place(x = 270, y = 550)
address_label2.place(x = 370, y = 550)
occupation_label1.place(x =270, y = 570)
occupation_label2.place(x = 370, y = 570)
criminal_record_label1.place(x = 270, y = 590)
criminal_record_label2.place(x = 370, y = 590)
description_label1.place(x = 270, y = 610)
description_label2.place(x = 370, y = 610)

root.mainloop()