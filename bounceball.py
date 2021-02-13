#bounce ball game
#kiruthika
import tkinter 
import random
from tkinter import*
from tkinter import messagebox
import os

root = Tk()

def exiit():
  root.destroy()
  import displaygame

width = 600
height = 600

canvas = Canvas(root, bg='ivory', width=width, height=height)
canvas.pack()

ball = canvas.create_oval(430, 10, 470, 50, fill='green')

platform_y = height - 20
platform = canvas.create_rectangle(width//2-50, platform_y, width//2+50, platform_y+10, fill='black')

# ball moving speed
xspeed = yspeed = 2

def move_ball():
  global xspeed, yspeed
  x1, y1, x2, y2 = canvas.coords(ball)
  if x1 <= 0 or x2 >= width:
    # hit wall, reverse x speed
    xspeed = -xspeed
  if y1 <= 0:
    # hit top wall
    yspeed = 2
  elif y2 >= platform_y:
    # calculate center x of the ball
    cx = (x1 + x2) // 2
    # check whether platform is hit
    px1, _, px2, _ = canvas.coords(platform)
    if px1 <= cx <= px2:
      yspeed = -2
    else:
      canvas.create_text(width//2, height//2, text='Game Over', font=('Arial Bold', 32), fill='red')
      return
  canvas.move(ball, xspeed, yspeed)
  canvas.after(20, move_ball)

def board_right(event):
  x1, y1, x2, y2 = canvas.coords(platform)
  # make sure the platform is not moved beyond right wall
  if x2 < width:
    dx = min(width-x2, 10)
    canvas.move(platform, dx, 0)

def board_left(event):
  x1, y1, x2, y2 = canvas.coords(platform)
  # make sure the platform is not moved beyond left wall
  if x1 > 0:
    dx = min(x1, 10)
    canvas.move(platform, -dx, 0)

canvas.bind_all('<Right>', board_right)
canvas.bind_all('<Left>', board_left)
b1=Button(root,text="Back to menu",command=exiit,font=("bold",10),bg="red").place(x=50,y=550)

move_ball()

root.mainloop()
