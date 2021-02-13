#display game
#kiruthika
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import re
import os
import sqlite3
import pygame
from pygame import mixer

def colo():
        root.destroy()
        import colorgame

def tik():
        root.destroy()
        import tiktoctoe

def bounce():
        root.destroy()
        import bounceball

def qiit():
        root.destroy()
        import loginfinal
def rate():
        root.destroy()
        import ratethisapp

def stop():
    pygame.mixer.music.stop()



    
root = Tk()
root.title("Game options")
canvas = Canvas(root, width = 1000, height = 667)
canvas.pack()
img3 = ImageTk.PhotoImage(Image.open("D:\\game project\\displayimg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img3)


form = Label(root,text="CHOOSE YOUR GAME",font=("bold",20),width=20,bg="violet")
form.place(x=100,y=70)

pygame.mixer.init()

photo2=PhotoImage(file="D:\game project\stopimgresize.png")
btn2=Button(root, image=photo2, command=stop,height=50,width=50)
btn2.place(x=800,y=600)
already=Label(root,text="Stop the music!",font=("italic",10),bg="yellow").place(x=700,y=600)

rritt=Button(root,command=stop).place(x=800,y=600)
color = Button(root,text="Rate this app",command=rate,font=("bold",10),bg="light green").place(x=350,y=600)
        
color = Button(root,text="Color game",command=colo,font=("bold",20),bg="light green").place(x=170,y=200)
tik = Button(root,text="Tik Toc Toe",command=tik,font=("bold",20),bg="brown").place(x=100,y=400)
bounce = Button(root,text="Bouncing ball",command=bounce,font=("bold",20),bg="purple").place(x=300,y=400)
back = Button(root,text="Back",command=qiit,font=("bold",10),bg="light yellow").place(x=150,y=600)
root.mainloop()

