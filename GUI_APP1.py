from tkinter import *
root = Tk()
root.title("GUI App1")
root.geometry("900x600")

# Create a Label Widget
mybutton = Button(root, text="Click Me", fg="black", bg="white", padx=20)    
mylabel = Label(root, text="My Label", borderwidth=5)
myEntry = Entry(root, width=50, borderwidth=5)
mytext = Text(root, width=50, height=10)
mybutton.pack(padx=10, pady=20)
mylabel.pack(padx=10, pady=5)
myEntry.pack(padx=10, pady=5)
mytext.pack(padx=10, pady=20)

# Store the value of the entry box
myGroup = StringVar()
op1 = Radiobutton(root, text="Option 1", variable=myGroup, value="Option 1").pack()
op2 = Radiobutton(root, text="Option 2", variable=myGroup, value="Option 2").pack()
op3 = Radiobutton(root, text="Option 3", variable=myGroup, value="Option 3").pack()
mycheckButton = Checkbutton(root, text="Check Me", variable=myGroup, onvalue="On", offvalue="Off").pack()


# Create a Listbox
myListbox = Listbox(root, selectmode=SINGLE, height=6, borderwidth=5)
myListbox.pack(padx=10, pady=20)

# Insert items into the Listbox
myListbox.insert(0, "Option 1")
myListbox.insert(1, "Option 2")
myListbox.insert(2, "Option 3")

root.mainloop()