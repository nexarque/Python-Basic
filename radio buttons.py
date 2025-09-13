import tkinter as tk

def show_choice():
    label.config(text="Select : "+ var.get())
    
root = tk.Tk()
root.geometry("300x200")

var = tk.StringVar(value="None")
radio1 = tk.Radiobutton(root,text="Option 1",variable=var, value="Option 1",command=show_choice)
radio2 = tk.Radiobutton(root,text="Option 2",variable=var, value="Option 2",command=show_choice)

radio1.pack()
radio2.pack()

label = tk.Label(root,text="Select an option")
label.pack()

root.mainloop()