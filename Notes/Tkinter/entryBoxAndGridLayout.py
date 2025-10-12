# Entry Box and Grid Layout

from tkinter import *

window = Tk()
window.geometry("350x50")
window.title("My Window")
window.configure(bg="yellow")

# Grid Layout
label1 = Label(window, text="mail")
label1.grid(row=0, column=1)

# Entry Box
Entry1 = Entry(window, width=40, borderwidth=3)
Entry1.grid(row=0, column=2)

label2 = Label(window, text="password")
label2.grid(row=1, column=1)

Entry2 = Entry(window, width=40, borderwidth=3)
Entry2.grid(row=1, column=2)

window.mainloop()
