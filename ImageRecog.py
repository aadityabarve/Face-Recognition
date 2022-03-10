from tkinter import *
import cv2
import numpy as np
import face_recognition
import os
from PIL import ImageTk,Image,ImageDraw
import sqlite3
from tkinter import ttk
from ttkthemes import themed_tk as tk

root=tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.geometry("1000x667")
f = ("Times bold", 14)
root.title("Face Recognised")
root.configure(background='Cadet Blue')

path = 'Images'
PplImages = []
PplName = []
myList = os.listdir(path)
for cl in myList:
    img = cv2.imread(f'{path}/{cl}')
    PplImages.append(img)
    PplName.append(os.path.splitext(cl)[0])
imgTest = cv2.imread(files_list)

def findFaceEncodings(PplImages):
    ImageEncodings = []
    for img in PplImages:
        img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        ImageEncodings.append(encode)
    return ImageEncodings

encodings = findFaceEncodings(PplImages)
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodingTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 255, 0), 2)

results = face_recognition.compare_faces(encodings,encodingTest)
faceDistances = face_recognition.face_distance(encodings,encodingTest)

minpos = 0
for i in range(0,len(results)):
    if faceDistances[minpos] > faceDistances[i]:
        minpos = i

print(PplName[minpos])
cv2.putText(imgTest, f'{PplName[minpos]}',(faceLocTest[3],faceLocTest[0]-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

cv2.imshow("Output", imgTest)
cv2.waitKey(4000)

identified_name=PplName[minpos]
imagePath = "Images/"+identified_name+".jpg"
image1 = Image.open(imagePath)
image1 = image1.resize((300, 300), Image.ANTIALIAS)
myImg = ImageTk.PhotoImage(image1)
label2 = ttk.Label(image=myImg, borderwidth=3, relief="ridge",)
label2.image = myImg
label2.place(x=350, y=180)
conn = sqlite3.connect('criminal_records.db')
c = conn.cursor()
query="SELECT * FROM people WHERE name='"+identified_name+"'"
c.execute(query)
list=c.fetchone()
print(list)
record=[]
for info in list:
    record.append(str(info))
global address
global occupation
global criminal_record
global description
print(record)
address=record[1]
occupation=record[2]
criminal_record=record[3]
description=record[4]
j=0
newDescription=""
for i in description:
    j=j+1
    if j==90:
        newDescription+="\n"
        j=0
    newDescription+=i
description=""
description=newDescription
print(description)
global address_label1
#canvas = Canvas(root, width=500, height=500)
#canvas.pack(fill=BOTH, expand=True)
# place the image inside canvas
#canvas.create_image(500, 333, image=myImg, anchor='center')
# resize function for resizing the image
# with proper width and height of root window
# canvas.create_text(500,90,fill="green",font="Arial 20 bold",
#                         text="Successfully Recognised!!! :)",anchor='center')
label = Label(root, text="SUCCESSFULLY RECOGNIZED!!",bd=21, font=("Arial Bold", 30),fg = 'Cornsilk', bg='Cadet Blue')
label.place(x = 240,y = 20)
percentage=round(percentage)
match_percentage=str(percentage)+"% MATCH"
percentage_label = Label(root, text=match_percentage, font=("Arial Bold", 30),fg = 'Cornsilk', bg='Cadet Blue')
percentage_label.place(x=380, y=90)
name_label1=Label(root, text="Name: ", font=("Arial Bold", 10), bg='Cadet Blue', fg='Cornsilk')
name_label2=Label(root, text=identified_name, font=("Arial Bold", 10), bg='Cadet Blue', fg='Cornsilk')
address_label1=Label(root, text="Address: ", font=("Arial Bold", 10), bg='Cadet Blue', fg='Cornsilk')
address_label2=Label(root, text=address, font=("Arial Bold", 10), bg='Cadet Blue', fg='Cornsilk')
occupation_label1=Label(root, text="Occupation: ", font=("Arial Bold", 10), bg='Cadet Blue', fg='Cornsilk')
occupation_label2=Label(root, text=occupation, font=("Arial Bold", 10), bg='Cadet Blue', fg='Cornsilk')
criminal_record_label1=Label(root, text="Criminal Record: ", font=("Arial Bold", 10), bg='Cadet Blue', fg='Cornsilk')
criminal_record_label2=Label(root, text=criminal_record, font=("Arial Bold", 10), bg='Cadet Blue', fg='Cornsilk')
description_label1=Label(root, text="Description: ", font=("Arial Bold", 10), bg='Cadet Blue', fg='Cornsilk')
description_label2=Label(root, text=description, font=("Arial Bold", 10), bg='Cadet Blue', fg='Cornsilk')
name_label1.place(x=230, y=530)
name_label2.place(x=400, y=530)
address_label1.place(x = 230, y = 550)
address_label2.place(x = 400, y = 550)
occupation_label1.place(x =230, y = 570)
occupation_label2.place(x = 400, y = 570)
criminal_record_label1.place(x = 230, y = 590)
criminal_record_label2.place(x = 400, y = 590)
description_label1.place(x = 230, y = 610)
description_label2.place(x = 400, y = 610)
conn.commit()
conn.close()