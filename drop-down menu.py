import tkinter as tk

def show_selection(*args):
    label.config(text="You selected:"+ variable.get())

root = tk.Tk()
root.geometry("300x200")

options = ["Python","Java","C++","Javascript"]
variable = tk.StringVar(value=options[0])
variable.trace("w",show_selection)

dropdown = tk.OptionMenu(root,variable,*options)
dropdown.pack(pady=20)

label = tk.Label(root,text="Select a language ")
label.pack()

root.mainloop()