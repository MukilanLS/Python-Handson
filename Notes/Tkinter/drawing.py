# Drawing

from tkinter import *

window = Tk()
window.title("My Window")

canvas = Canvas(window, width=500, height=500, bg="white")
canvas.pack()

canvas.create_line(0, 0, 500, 500, width=5 ,fill="red",dash=(3,3))
canvas.create_line(0, 500, 500, 0, width=5 ,fill="blue",dash=(3,3))
canvas.create_rectangle(125, 150, 450, 375, width=5 ,fill="yellow", outline="black",dash=(3,3))

window.mainloop()
