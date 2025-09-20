import tkinter as tk

def show_text():
    text_content  = text.get("1.0",tk.END)
    label.config(text = "Your wrote:\n" + text_content)
    
root= tk.Tk()
root.geometry("300x300")

text = tk.Text(root,height=5,width=30)
text.pack(pady=10)

button = tk.Button(root,text="Show text",command=show_text)
button.pack()

label = tk.Label(root,text="")
label.pack()

root.mainloop()
