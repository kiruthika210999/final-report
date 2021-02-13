#register game page 
#kiruthika
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import pyglet
import re
import os
import sqlite3


def registers():
    root.destroy()
    import gamelogin

   
    
class registerSet:
    def __init__(self,root):

        self.root = root

        self.root.title("Wise Gaming Registration")

        self.canvas = Canvas(root, width = 700,height = 700)
        self.canvas.pack()
        self.img1 = ImageTk.PhotoImage(Image.open("D:\game project\img1.jpg"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.img1)

        form=Label(root,text="Gaming application",width=20,font=("Algerian",20))
        form.place(x=90,y=60)

        label_1=Label(root,text="Emailid",font=("bold",10),width=10)
        label_1.place(x=70,y=130)
        self.txt_email = Entry()
        self.txt_email.place(x=250, y=130)

        label_2=Label(root,text="Password",font=("bold",10))
        label_2.place(x=70,y=180)
        self.txt_pswd = Entry(show="*")
        self.txt_pswd.place(x=250, y=180)

        label_3=Label(root,text="Confirm password",font=("bold",10),width=15)
        label_3.place(x=70,y=230)
        self.txt_cemail = Entry(show="*")
        self.txt_cemail.place(x=250, y=230)

        label_4=Label(root,text="age",font=("bold",10))
        label_4.place(x=70,y=280)
        self.txt_age = Entry()
        self.txt_age.place(x=250, y=280)

        
        
        register = Button(root,text="Register",command = self.commy,font=("bold",10),bg="gray").place(x=200,y=600)
        already=Button(root,relief=FLAT,text="If already exists user",font=("bold",10)).place(x=450,y=600)
        login=Button(root,text="Login",command=registers,bg="brown",font=("bold",10)).place(x=550,y=600)
        exiit=Button(root,text="EXIT",command=self.callnewscreen,bg="light blue",font=("bold",10)).place(x=350,y=600)
    
            
    def validate_email(self,email):
        if len(email) > 8 :
            if re.match("^[a-zA-Z0-9]+[@]+[a-z][A-Z][0-9].[a-z]",email)!=None:
                return True
            return False
        else:
            messagebox.showinfo("Information","write in correct format")
    

    def validate_password(self,pswd):     
        if len(pswd) > 8:
            if re.match("a-zA-Z0-9!@#$%^&*?<>?",pswd):
                return True
            return False
        else:
            messagebox.showinfo("Information","need one upper case,lower case,number and special characters")
        
        
    def validate_conpass(self,cemail):
        if len(cemail)>8:
            if re.match("a-zA-Z0-9!@#$%^&*?<>?",cemail):
                return True
            return False
        else:
            messagebox.showinfo("Information","mismatch")


    def validate_age(self,age):
        if age.isnumeric():
            return True
        else:
            messagebox.showinfo("Information","Grow big and play with us")

        
    def validate(self):
        if self.txt_email.get()=="":
            messagebox.showinfo("Information","Email Id is mandatory")
        elif self.txt_email.get()!="":
            status1=self.validate_email(self.txt_email.get())

        if self.txt_pswd.get()=="":
            messagebox.showinfo("Information","Password is mandatory")
        elif self.txt_pswd.get()!="":
            status2=self.validate_password(self.txt_pswd.get())

        if self.txt_cemail.get()=="":
            messagebox.showinfo("Information","Confirm Password is mandatory")
        elif self.txt_cemail.get()!="":
            status3=self.validate_conpass(self.txt_cemail.get())            

        if self.txt_age.get()=="":
            messagebox.showinfo("Information","Age is mandatory")
        elif self.txt_age.get()!=5:
            status4=self.validate_age(self.txt_age.get())
        else:
            messagebox.showinfo("Information","Successfully registered for gaming")
            
        
    def commy(self):
        global conn,cursor
        mail=self.txt_email.get()
        pswd=self.txt_pswd.get()
        lastform=self.validate()
        
        conn = sqlite3.connect('content.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS design(MAIL TEXT,PASSWORD TEXT)''')
        cursor.execute("INSERT INTO design(MAIL,PASSWORD) VALUES(?,?)",(mail,pswd,))
        print("Table is created")
        conn.commit()

    def callnewscreen(self):
        self.destroy()
        os.system("Registered successfully")
    

root=Tk() 
objSet=registerSet(root)
root.mainloop()
