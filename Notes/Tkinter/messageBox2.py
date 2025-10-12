# Message Box 2
from tkinter import *

window = Tk()
window.title("My Window")
window.geometry("500x500")

message = Message(window, text="Hello World")
message.pack()

var = StringVar()
message2 = Message(window, textvariable=var, relief = RAISED, padx= 50, pady = 50)
var.set("Welcome!")
message2.pack()

var2 = StringVar()
ent_Var = StringVar()

def Insert():
    result = ent_Var.get()
    var2.set(result)

message3 = Message(window, textvariable=var2, relief = RAISED, padx= 50, pady = 50)
message3.pack()

entry = Entry(window, textvariable=ent_Var)
entry.pack()

button = Button(window, text="OK", command = Insert)
button.pack()

mainloop()