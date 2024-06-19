
from tkinter import *

base = Tk()  
base.geometry('500x500')  
base.title("Registration Form")

def pushed(str:str):
    print(str.get().upper())

def draw(function):
    Label(base, text="Login").pack()
    Label(base, text="Name").pack()
    textbox = StringVar()
    Entry(base, textvariable=textbox).pack()
    Button(base, text="Submit",command=lambda: function(textbox)).pack()
    base.mainloop()

def test():
    draw(pushed)
test()