import tkinter as tk

def show_selection(event):
    selection = listbox.get(listbox.curselection()[0])
    label.config(text="Selected: " + selection)
    
root = tk.Tk()
root.geometry("300x200")

listbox = tk.Listbox(root)
listbox.insert(1,"Apple")
listbox.insert(2,"Banana")
listbox.insert(3,"Cherry")
listbox.pack()
listbox.bind('<<ListboxSelect>>',show_selection)

label = tk.Label(root,text="Choose a Fruit ")
label.pack()

root.mainloop()