from tkinter import *

root = Tk()

label = Label(root, text="Blue", bg='blue', fg='white')
label.pack(fill=X)
label1 = Label(root, text="Red", bg='red', fg='white')
label1.pack(fill=X)
label2 = Label(root, text="Black", bg='black', fg='white')
label2.pack(expand=True, fill=Y)

root.geometry('200x200')

root.mainloop()
