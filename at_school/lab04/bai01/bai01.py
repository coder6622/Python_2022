# todo: gioi thieu ve tkinter

from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Style, Button


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.style = None
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Hello Long")
        self.style = Style()
        self.style.theme_use("classic")

        self.pack(fill=BOTH, expand=1)

        quit_button = Button(self, text="Quit", command=self.quit,
                             cursor="plus")
        quit_button.place(x=50, y=50)


root = Tk()
root.geometry("300x300+600+200")
app = Example(root)
root.mainloop()
