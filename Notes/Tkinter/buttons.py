# Handling Buttons

from tkinter import *

window = Tk()
window.title("My Window")
window.geometry("500x500")

def log_entry():
    print("Logged in")

button1 = Button(window, text="LOGIN", bg="red", fg="white",
                 command=log_entry, width=20, font=("Arial", 20, "bold"), activebackground="black",
                 activeforeground="white")
button1.pack()

window.mainloop()
