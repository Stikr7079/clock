from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("SATISH")
root.geometry("1350x250")

def time():
    string = strftime('%H:%M:%S: %p')  #time format
            #%H	Hour (24-hour clock) as a decimal number [00,23].
            #%M	Minute as a decimal number[00,59].
            #%S	Second as a decimal number[00,61].
            #%p	Locale’s equivalent of either AM or PM.
         
    label.config(text=string)
    label.after(1000, time)   #time delay of 1000 milliseconds


label = Label(root , font=("ds-digital", 170), background="white", foreground="green")
label.pack(anchor='center')

time()
mainloop()
