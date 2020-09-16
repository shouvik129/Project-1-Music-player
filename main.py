import pygame
import tkinter as tkr
import os

player =tkr.Tk()
player.title("Music player")
player.geometry("280x340")
os.chdir("E:\music folder")
print(os.getcwd)
songlist = os.listdir
VolumeLevel=tkr.Scale(player,from_=0,to_=10,orient=tkr.HORIZONTAL,resolution=0.01)
playlist = tkr.Listbox(player,highlightcolor="red",selectmode=tkr.SINGLE)
print(songlist)
for item in songlist():
    pos=0
    playlist.insert(pos,item)
    pos=pos+1
pygame.init()
pygame.mixer.init()
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get())
    print(pygame.mixer.music.set_volume)
    print(VolumeLevel.get())
def Exitplayer():
    pygame.mixer.music.stop()
def Pause():
    pygame.mixer.music.pause()
def UnPause():
    pygame.mixer.music.unpause()
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=play)
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=Exitplayer)
button3 = tkr.Button(player, width=5, height=3, text="PAUSE", command=Pause)
button4 = tkr.Button(player, width=5, height=3, text="UNPAUSE", command=UnPause)
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)
songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
VolumeLevel.pack(fill="x")
playlist.pack(fill="both", expand="yes")
player.mainloop()
