# todo: layout trong tkinter
import os
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Style, Label

from PIL import Image, ImageTk


class Example(Frame):
    path1 = 'layout'
    dirlist = os.listdir(path1)

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Hello Long")

        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        bard = Image.open(os.path.join(self.path1, 'pause-autorotate.png'))
        bard = bard.resize((100, 100), )
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)

        rot = Image.open(os.path.join(self.path1, "minimize-3d.png"))
        rot = rot.resize((100, 100), )
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)

        minc = Image.open(os.path.join(self.path1, "pause-autorotate.png"))
        minc = minc.resize((100, 100), )
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)


root = Tk()
root.geometry("300x300+600+200")
app = Example(root)
root.mainloop()
