# Message Box 1
import tkinter.messagebox
from tkinter import *

window = Tk()
window.title("My Window")
window.geometry("500x500")

tkinter.messagebox.showinfo("Info", "Running out of time")
tkinter.messagebox.showwarning("Warning", "Running out of time")
tkinter.messagebox.showerror("Error", "Running out of time")
tkinter.messagebox.askokcancel("Info", "Running out of time")
tkinter.messagebox.askquestion("Weather", "Will it rain?")

askyesno = tkinter.messagebox.askyesno("Weather", "Will it rain?")
if askyesno:
    print("Use an Umbrella")
else:
    print("Okay")

mainloop()