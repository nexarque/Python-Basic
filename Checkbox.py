import tkinter as tk

def show_choice():
    label.config(text="Selected : "+str(var.get()))
    
root = tk.Tk()
root.geometry("300x200")

var = tk.IntVar()
checkbox = tk.Checkbutton(root,text="Click me",variable=var,command=show_choice)
checkbox.pack(pady=20)

label = tk.Label(root,text="Select checkbox")
label.pack()

root.mainloop()

















