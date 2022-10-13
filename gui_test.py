import tkinter as tk

root = tk.Tk()
root.title("Funny GUI")
root.resizable(width=False, height=False)
root.geometry("600x800")
root.configure(bg="grey")

l = tk.Label(root, text="Bruh", bg="grey", fg="black", font=("Arial", 25))
l.grid(row=0, column=0)

username = tk.Text(root, width=25, height=1)
username.grid(row=1, column=0)

def buttonclicked():
    message = username.get(1.0, "end-1c")
    l2.config(text = message)

l2 = tk.Label(root, text="")
l2.grid(row=2, column=0)

submit = tk.Button(root, text="Submit", command = buttonclicked)
submit.grid(row=3, column=0)

root.mainloop()
