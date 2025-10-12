# Place

from tkinter import *

window = Tk()
window.title("My Window")
window.geometry("500x500")

button = Button(window, text= "Button", width =20,)
button.place(x=200, y=200)

window.mainloop()
