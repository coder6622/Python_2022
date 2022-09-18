from tkinter import RAISED, BOTH, RIGHT, Tk
from tkinter.ttk import Frame, Style, Button


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.style = None
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Button")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        close_btn = Button(self, text="Close", command=self.quit)
        close_btn.pack(side=RIGHT, padx=10, pady=10)

        ok_btn = Button(self, text="OK")
        ok_btn.pack(side=RIGHT)


root = Tk()
root.geometry("300x300+300+300")
app = Example(root)
app.mainloop()
