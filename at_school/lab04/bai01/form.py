from tkinter import *


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.style = None
        self.initUI()

    def initUI(self):
        self.parent.title("Form Example")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)
        frame1.grid_rowconfigure(0, weight=5)

        lbl1 = Label(frame1, text="Title", width=6)
        lbl1.grid(row=0, column=0)

        entry1 = Entry(frame1)
        entry1.grid(row=0, column=1)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Auther", width=6)
        lbl2.grid(row=0, column=0)

        entry2 = Entry(frame2)
        entry2.grid(row=0, column=1)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.grid(row=0, column=0)

        entry3 = Entry(frame3)
        entry3.grid(row=0, column=1)


root = Tk()
# root.geometry('300x300+300+300')
app = Example(root)
# app.grid_columnconfigure(0, weight=100)
# root.grid_rowconfigure(0, weight=2)
app.mainloop()
