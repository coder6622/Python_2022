from tkinter import BOTH, Tk, Entry, X, LEFT, CENTER
from tkinter.ttk import Frame, Label


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.style = None
        self.initUI()

    def initUI(self):
        self.parent.title("Form Example")
        self.pack(fill=BOTH, expand=1)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Title", width=6)
        lbl1.pack(side=LEFT, pady=5, padx=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Auther", width=6)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=CENTER, padx=5, pady=5)

        entry3 = Entry(frame3)
        entry3.pack(fill=BOTH, padx=5, pady=5, expand=True)


root = Tk()
root.geometry('300x300+300+300')
app = Example(root)
app.mainloop()
