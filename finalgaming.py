#introduction page
#kiruthika
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import pyglet
import tkinter as tk
import re
import os
import pygame
from pygame import mixer



def nexxt():
    root.destroy()
    import registergame


root = tk.Tk()
root.title("Wise gaming")
canvas = Canvas(root, width = 1000, height = 667)
canvas.pack()
img3 = ImageTk.PhotoImage(Image.open("D:\\game project\\frontimage.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img3)

pygame.mixer.init()

def play():
    pygame.mixer.music.load("D:\game project\Master-the-Blaster-MassTamilan.io.mp3")
    pygame.mixer.music.play(loops=0)
def stop():
    pygame.mixer.music.stop()

photo1=PhotoImage(file="D:\game project\playimgresize.png")
btn1=Button(root, image=photo1, command=play,height=50,width=50)
btn1.place(x=550,y=600)

already=Label(root,text="Lets! play music",font=("italic",10),bg="blue").place(x=450,y=620)

photo2=PhotoImage(file="D:\game project\stopimgresize.png")
btn2=Button(root, image=photo2, command=stop,height=50,width=50)
btn2.place(x=800,y=600)

rri=Button(root,command=play).place(x=550,y=600)
rritt=Button(root,command=stop).place(x=800,y=600)

form=Label(root,text="Wise Gaming Introduction",width=20,font=("Algerian",20))
form.place(x=160,y=40)


para1=Label(root,text="Hey Bonda's,",font=("italian",13),foreground="red")
para1.place(x=0,y=100)
para2=Label(root,text="""This is wise gaming designed by kiruthika.
            Gaming actually boost your brain power and gaming imporves your problem solving.Mainly gaming relief your
            stress and increase your concentration.Playing mobilegames has been shown to provide certain health benefits
            including, reducing,depression,stress and even raising dopamine levels whichis what makes you feel good when
            you're playing and winning.Here wise gaming gives you four different games which is more interesting""",
             font=("bold",12),foreground="gray")
para2.place(x=40,y=130)
para3=Label(root,text="Color Game:",font=("italian",11),foreground="green")
para3.place(x=0,y=230)
para4=Label(root,text="""Bonda's This a simple game where the player should press the 'enter' button to start the game.
            Then the colours will display in the screen.Then name of the colour is different and the text colour is different.
            This is the twist in this game. The player should type the 'text colour' and the score will add according to your
            correct answer.""",font=("bold",12),foreground="gray")
para4.place(x=40,y=260)
para5=Label(root,text="TikTocToe:",font=("italian",11),foreground="violet")
para5.place(x=0,y=340)
para6=Label(root,text="""Bonda's This is a game we played in our notebook with friends in schooldays.Here the game instructions:
            There are 2 variable 'x'and'o' here the play area gives you 3x3 square space where the players are going to play.
            The player click any one box the box is filled with 'x' and clicking on another box it will display 'o'. Player
            should fill the total box. If the 'x' repeated for 2 times in order of row or column or cross way then x will be the
            winner and this suited for 'o' also. And the main thing is the match can be 'draw' when the x and o are not in the
            joined in rules of tiktoctoe.""",font=("bold",12),foreground="gray")
para6.place(x=40,y=370)
para7=Label(root,text="Bouncing Ball:",font=("italian",11),foreground="orange")
para7.place(x=0,y=490)
para8=Label(root,text="""Bonda's This is the game we have played in our childhood days in button phone. Here there will be a ball,
            a surface and rectangle tool. The ball will thrown from the top, it will keep on moving and the player should move the
            rectangle tool using right and left key. Player shouldn't make ball to touch the surface. If the ball touch the surface
            the game will end. By the time increases the speed of the ball also increase the player should keep on make the ball to bounce.""",
            font=("bold",12),foreground="gray")
para8.place(x=40,y=520)


rrit=Button(root,text="Are you ready to play",command=nexxt,font=("bold",10),bg="violet").place(x=200,y=620)

root.mainloop()

