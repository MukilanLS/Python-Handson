import tkinter as tk

def press(char):
    entry_var.set(entry_var.get() + str(char))

def clear():
    entry_var.set("")

def equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except Exception:
        entry_var.set("Error")

root = tk.Tk()
root.title("Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 16), width=23, borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2, 2),  # The last value is columnspan=2
    ('C', 5, 0), ('=', 5, 1, 3)  # The last value is columnspan=3
]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    # Default columnspan is 1
    column_span = btn[3] if len(btn) == 4 else 1

    if text == '=':
        cmd = equal
    elif text == 'C':
        cmd = clear
    else:
        cmd = lambda t=text: press(t)

    tk.Button(root, text=text, width=6 * column_span, height=2, font=("Arial", 12), command=cmd).grid(
        row=row, column=col, columnspan=column_span, padx=2, pady=2, sticky="nsew"
    )

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
