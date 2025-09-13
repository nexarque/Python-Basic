import tkinter as tk

def calculate():
    result = float(entry1.get()) + float(entry2.get())
    label.config(text="Result : " + str(result))
    
root = tk.Tk()
root.geometry("300x200")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

button = tk.Button(root,text="Add ",command=calculate)
button.pack(pady=5)

label = tk.Label(root,text="Result")
label.pack()

root.mainloop()
