# Calculator

from tkinter import *

window = Tk()
window.title("My Window")
window.geometry("300x400")

entry = Entry(window, width=22, borderwidth=5, font=("Arial", 16), justify= "left")
entry.place(x=0, y=0)

def button_clicked(number):
    result = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(result) + str(number))

def addition():
    n1 = entry.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    entry.delete(0, END)

def subtraction():
    n2 = entry.get()
    global math
    math = "subtraction"
    global i
    i = int(n2)
    entry.delete(0, END)

def multiplication():
    n3 = entry.get()
    global math
    math = "multiplication"
    global i
    i = int(n3)
    entry.delete(0, END)

def division():
    n4 = entry.get()
    global math
    math = "division"
    global i
    i = int(n4)
    entry.delete(0, END)

def equal():
    n5 = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, i+int(n5))
    elif math == "subtraction":
        entry.insert(0, i-int(n5))
    elif math == "multiplication":
        entry.insert(0, i*int(n5))
    elif math == "division":
        entry.insert(0, i/int(n5))

def clear():
    entry.delete(0, END)

button_1= Button(window, text="1", width=12, anchor="center", command=lambda: button_clicked(1))
button_1.place(x=10, y=60)
button_2 = Button(window, text="2", width=12, anchor="center",command=lambda: button_clicked(2))
button_2.place(x=80, y=60)
button_3 = Button(window, text="3", width=12, anchor="center", command=lambda: button_clicked(3))
button_3.place(x=170, y=60)

button_4 = Button(window, text="4", width=12, anchor="center", command=lambda: button_clicked(4))
button_4.place(x=10, y=120)
button_5 = Button(window, text="5", width=12, anchor="center", command=lambda: button_clicked(5))
button_5.place(x=80, y=120)
button_6 = Button(window, text="6", width=12, anchor="center", command=lambda: button_clicked(6))
button_6.place(x=170, y=120)

button_7 = Button(window, text="7", width=12, anchor="center", command=lambda: button_clicked(7))
button_7.place(x=10, y=180)
button_8 = Button(window, text="8", width=12, anchor="center", command=lambda: button_clicked(8))
button_8.place(x=80, y=180)
button_9 = Button(window, text="9", width=12, anchor="center", command=lambda: button_clicked(9))
button_9.place(x=170, y=180)

button_0 = Button(window, text="0", width=12, anchor="center", command=lambda: button_clicked(0))
button_0.place(x=10, y=240)
button_add = Button(window, text="+", width=12, anchor="center", command=lambda: addition())
button_add.place(x=80, y=240)
button_sub = Button(window, text="-", width=12, anchor="center", command=lambda: subtraction())
button_sub.place(x=170, y=240)

button_mul = Button(window, text="*", width=12, anchor="center", command=lambda: multiplication())
button_mul.place(x=10, y=300)
button_div = Button(window, text="/", width=12, anchor="center", command=lambda: division())
button_div.place(x=80, y=300)
button_equal = Button(window, text="=", width=12, anchor="center", command=lambda: equal())
button_equal.place(x=170, y=300)

button_clear = Button(window, text="C", width=12, anchor="center", command=clear)
button_clear.place(x=10, y=350)

window.mainloop()
