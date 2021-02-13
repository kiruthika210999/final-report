#rate this app
#kiruthika
from tkinter import*
import tkinter as tk 
from tkinter import ttk 
import os
import sqlite3
def exiit():
    root.destroy()
    import displaygame

root=Tk()
root.title("Rate this app")
root.geometry("400x200")

ttk.Label(root, text = "Select your option :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 5, pady = 10) 
  
n = tk.StringVar() 
rateapp = ttk.Combobox(root, width = 27, textvariable = n) 
  
rateapp['values'] = ('good',
                          'medium',
                          'bad') 
  
rateapp.grid(column = 1, row = 5) 
rateapp.current() 

b1=Button(root,text="Back to menu",command=exiit,font=("bold",10),bg="red").place(x=50,y=100)

root.mainloop()
