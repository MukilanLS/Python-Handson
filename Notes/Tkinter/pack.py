# Pack

from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("My Window")

label1 = Label(window, text="Label-1", fg="red", bg="black")
label1.pack(side=TOP, fill=X, expand=False)

label2 = Label(window, text="Label-2", fg="yellow", bg="orange")
label2.pack(side=BOTTOM, fill=X, expand=False)

label3 = Label(window, text="Label-3", fg="green", bg="pink")
label3.pack(side=LEFT, fill=Y, expand=False)

label4 = Label(window, text="Label-4", fg="cyan", bg="blue")
label4.pack(side=RIGHT, fill=Y, expand=False)

window.mainloop()