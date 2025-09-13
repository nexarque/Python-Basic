import tkinter as tk

root = tk.Tk()
root.title("Simple Window")
root.geometry("300x200")

label = tk.Label(root,text="Hello, Tkinter!")
label.pack(pady=50)

root.mainloop()