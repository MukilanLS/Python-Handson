# Check Box 1

from tkinter import *

window = Tk()
window.title("My Window")
window.geometry("500x500")

checkBox1 = IntVar()
checkBox2 = IntVar()
checkBox3 = BooleanVar()

check_button1 = Checkbutton(window, text="Apple", onvalue=1, offvalue=0, height= 2, width=10, variable=checkBox1)
check_button1.pack()
check_button2 = Checkbutton(window, text="Mango", onvalue=1, offvalue=0, height= 2, width=10, variable=checkBox2)
check_button2.pack()
check_button3 = Checkbutton(window, text="Grapes", onvalue=1, offvalue=0, height= 2, width=10, variable=checkBox3)
check_button3.pack()

window.mainloop()