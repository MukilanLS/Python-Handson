# TKINTER

# Step 1: Import Tkinter
# Step 2: GUI Interaction
# Step 3: Adding Inputs
# Step 4: Main Loop

from tkinter import *

window = Tk()
window.geometry("500x700")
window.title("My Window")
window.configure(bg="yellow")

inp = Label(window, text="Hello World")
inp.config(bg="red")
inp.pack()

frame1 = Frame(window, bg="white", width=300, height=300, cursor="dot")
frame1.pack(side = TOP)

frame2 = Frame(window, bg="purple", width=300, height=300, cursor="dotbox")
frame2.pack(side = BOTTOM)

button1 = Button(frame1, text="Click Me", bg="green", fg="white")
button1.pack()

button2 = Button(frame2, text="Click Me", bg="red", fg="white")
button2.pack()

button3 = Button(frame1, text="Click Me", bg="purple", fg="white")
button3.pack()

window.mainloop()
