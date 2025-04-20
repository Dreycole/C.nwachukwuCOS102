import tkinter as tk
from tkinter import messagebox as msgbox

#handling button click event 
def button_click():
    #show an informaation message box
    msgbox.showinfo("info","welcome to COS 102 GUI app!\n")

    #ask for user confirmation
    result=msgbox.askyesno("comnfirmation","to you want to continue")

#create the main window
root=tk.Tk()
root.title("home page")
root.geometry("300x100")

#add a label widget
label=tk.Label(root,text="hello friend\n")
label.pack()

#add button widget
button =tk.Button(root,text="click Me!",command=button_click)
button.pack()

#styling the button widget
button.config(fg="red", bg="yellow")

#start the event loop
root.mainloop()



