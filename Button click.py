import tkinter as tk

def on_click():
    label.config(text="Button Clicked")
    
root = tk.Tk()
root.geometry("300x200")
    
label = tk.Label(root,text="Press the button")
label.pack(pady=20)
    
button = tk.Button(root,text="Click me, command=on click")
button.pack()
    
root.mainloop()