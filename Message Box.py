import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Info", "Hello! this is a message box")

root = tk.Tk()
root.geometry("300x200")

button = tk.Button(root,text="show message ",command=show_message)
button.pack(pady=50)

root.mainloop()
