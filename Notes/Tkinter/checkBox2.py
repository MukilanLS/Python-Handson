# Check Box 2

from tkinter import *

def show_order_summary():
    summary_text = "Your Order:\n"
    # Get the state of each Checkbutton using its associated variable
    if pizza_var.get() == 1:  # Check if onvalue (1) is set
        summary_text += "- Pizza\n"
    if pasta_var.get() == 1:
        summary_text += "- Pasta\n"
    if salad_var.get() == 1:
        summary_text += "- Salad\n"

    if summary_text == "Your Order:\n":  # If nothing selected
        summary_text = "No items selected."

    summary_label.config(text=summary_text)

root = Tk()
root.title("Order Options")
root.geometry("300x300")
Label(root, text="Select your items:", font=("Arial", 14,
                                                "bold")).pack(pady=10)
# Create IntVar variables to hold the state of each Checkbutton
pizza_var = IntVar()
pasta_var = IntVar()
salad_var = IntVar()
# Create Check buttons, associating each with its variable
# onvalue=1, offvalue=0 are defaults for IntVar, explicitly included for clarity
pizza_cb = Checkbutton(root, text="Pizza", variable=pizza_var,
                          onvalue=1, offvalue=0, font=("Arial", 12))
pizza_cb.pack(anchor=W, padx=20)  # Align to West (left)

pasta_cb = Checkbutton(root, text="Pasta", variable=pasta_var,
                          onvalue=1, offvalue=0, font=("Arial", 12))
pasta_cb.pack(anchor=W, padx=20)
salad_cb = Checkbutton(root, text="Salad", variable=salad_var,
                          onvalue=1, offvalue=0, font=("Arial", 12))
salad_cb.pack(anchor=W, padx=20)
# Button to show selected items
summary_button = Button(root, text="Show Order Summary",
                           command=show_order_summary)
summary_button.pack(pady=20)
# Label to display the summary
summary_label = Label(root, text="")
summary_label.pack()
root.mainloop()
