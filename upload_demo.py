from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os, shutil

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("thinter Dialog Widget")
        self.minsize(640,400)

        self.labelFrame = ttk.LabelFrame(self,text="Open A File")
        self.labelFrame.grid(column=0,row=1,padx= 20, pady= 20)
        self.btton()

    def btton(self):
        self.button = ttk.Button(self.labelFrame, text="Browse", command=self.fileDailog)
        self.button.grid(column=1,row=1)
    def fileDailog(self):
        self.fileName = filedialog.askopenfilename(initialdir = "/", title="Select A File",filetype=(("jpeg","*.jpg"),("png","*.png")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column =1,row = 2)
        self.label.configure(text = self.fileName)
        os.chdir('e:\\')
        os.system('mkdir BACKUP')
        shutil.move(self.fileName,'e:\\')



if __name__ == '__main__':
    root = Root()
    root.mainloop()