import tkinter as tk
from tkinter import ttk
from functools import partial

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current+value)


def clear():
    entry.delete(0, tk.END)


def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))


root = tk.Tk()
root.title('Calculator')

entry = tk.Entry(root, font=('Helvetica', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text,row,column) in buttons:
    if text == '=':
        button = ttk.Button(root, text=text, command=calculate)
    else:
        button = ttk.Button(root, text=text, command=partial(button_click, text))

    button.grid(row=row, column=column, padx=5, pady=5, sticky='ew')

clear_button = tk.Button(root, text='C', command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky='ew')

root.mainloop()


