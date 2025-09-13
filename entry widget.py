import tkinter as tk

def show_text():
    label.config(text="You entered "+ entry.get())
    
root = tk.Tk()
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack(pady=20)

button =tk.Button(root,text="Submit",command=show_text)
button.pack()

label = tk.Label(root,text="")
label.pack()

root.mainloop()