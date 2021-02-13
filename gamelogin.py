#game login page
#kiruthika
from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import pyglet
import re
import os
import sqlite3
from winsound import *

root = Tk()
root.title("Login page")
canvas = Canvas(root, width = 400,height = 400)
canvas.pack()
img2 = ImageTk.PhotoImage(Image.open("D:\game project\game-login.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img2)

        
form = Label(root,text="Login",font=("bold",20),width=20)
form.place(x=50,y=70)
            

def logins():
        root.destroy()
        import displaygame

def quiit():
        root.destroy()
        import registergame

def show():
    if var.get()==1:
        entry2.configure(show="")
    elif var.get()==0:
        entry2.configure(show="*")


email_id=StringVar()
pass_word=StringVar()

emailid=Label(root,text="Emailid",font=("bold",10),width=10)
emailid.place(x=70,y=130)
entry1 = Entry(root,textvariable=email_id,font=("bold",10))
entry1.place(x=170, y=130)

password=Label(root,text="Password",font=("bold",10))
password.place(x=70,y=180)
entry2 = Entry(root,show="*",textvariable=pass_word,font=("bold",10))
entry2.place(x=170, y=180)

var=IntVar()
photo2=PhotoImage(file="D:\game project\eyeimgresize.png")
btn1=Checkbutton(root,image=photo2,command=show,offvalue=0,onvalue=1,variable=var,relief=FLAT,bg="White")
btn1.place(x=320,y=180)
    
def long():
        if email_id.get()=="" or pass_word.get()=="":
                messagebox.showwarning("Information","This field is empty")
        else:
                conn=sqlite3.connect('content.db')
                cur = conn.cursor()
                cur.execute("SELECT MAIL,PASSWORD FROM design WHERE MAIL=? and PASSWORD=?",(email_id.get(),pass_word.get()))
                
                if cur.fetchone() is not None:
                    logins()
                    
                else:
                    messagebox.showinfo("Information","Invalid emailid and password")



            
login= Button(root,text="Login",command=long,font=("bold",10),bg="light pink").place(x=180,y=250)
back = Button(root,text="Back",command=quiit,font=("bold",10),bg="gray").place(x=110,y=250)

root.mainloop()
