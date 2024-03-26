from tkinter import Tk, Label
import time 
import sys

mainTime = Tk()
mainTime.title("my Digital clock")

def get_time():
    timevar = time.strftime("%I:%M:%S %p")
    clock.config(text=timevar)
    clock.after(20, get_time)
clock = Label(mainTime, font=("Calibri", 90), bg="black", fg="white")
clock.pack()   

get_time()
mainTime.mainloop()

