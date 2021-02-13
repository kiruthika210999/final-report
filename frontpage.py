#wise gaming
#project
#kiruthika
from tkinter import*
import pyglet
def dis():
    root.destroy()
    import finalgaming

root=Tk()
root.title("gaming video")
root.geometry("200x200")

vidpath="D:\game project\InShot_20210202_075008294.mp4"
window=pyglet.window.Window()
player=pyglet.media.Player()
source=pyglet.media.StreamingSource()
MediaLoad=pyglet.media.load(vidpath)

player.queue(MediaLoad)
player.play()

@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(50,50)

pyglet.app.run()

b1=Button(root,text="Go to the game",command=dis,bg="white").place(x=60,y=100)
root.mainloop()
