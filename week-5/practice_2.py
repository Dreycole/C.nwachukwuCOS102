import tkinter as tk
from tkinter import messagebox
from PIL import image, imageTK

def welcomeMessage(username):
    #create a Tkinter window 
    window=tk.toplevel(root)
    window.geometry("500*200")

    label_1=tk.label(window, text=f"welcome{username}\n")
    label_1.pack()
    label_2=tk.Label(Window,text="this is python GUI with Tkinter")
    label_2.pack()

    #run the Tkinter event loop
    root.mainloop()

    def submit():
        username=username_entry.get()
        password=password_entry.get()

        if username=="mary" and password=="cos102":
         welcomeMessage(username)
        else:
           messagebox.showerror("login","invlaid username or password")