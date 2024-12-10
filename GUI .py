from tkinter import *
from tkinter import ttk
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
def read_text():
    text = Entry.get(myEntry)
    engine.say(text)
    engine.runAndWait()

def delete_text():
    myEntry.delete(0, END)


myFrame = Tk()
myFrame.title("Text To Speech")
myFrame.geometry("500x400")

myLabel1 = Label(myFrame, text="Text To Speech", font="Tahoma 30 bold")
myLabel2 = Label(myFrame, text="Enter Your Text", font= "Tahoma 15 bold", pady=30, padx=10)

myEntry = Entry(myFrame, width=50)

# Create Buttons 
Button1 = ttk.Button(myFrame, text="Play", command=read_text) 
Button2 = ttk.Button(myFrame, text="Set", command= delete_text)
Button3 = ttk.Button(myFrame, text="Exit", command=exit)

myLabel1.pack()
myLabel2.pack()
myEntry.pack()
Button1.pack(side=TOP, pady=25)
Button2.pack(side=TOP, pady=25)
Button3.pack(side=TOP, pady=25)
myFrame.mainloop()