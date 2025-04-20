#Create main window
root = tk.Tk()
root.title("Login form")
root.geometry("500x200")

#create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

#create password label and entry
password_label = tk.Label(root, text="password:")
password_label.pack()
password_entry = tk.Entry(root,show="*")
password_entry.pack()

#create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

#run the main event loop 
root.mainloop()


