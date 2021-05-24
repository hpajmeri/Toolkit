import os
import webbrowser
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import pygame



#---------Making the Window and Frames----------
root = Tk()
frame1 = Frame(root)
menu = Menu(frame1)
root.config(menu=menu)
root.title("Music Player V1")




# ---------functions-------------
root.filename=""
root.playlist = []
root.pauseFlag = False
root.songAdded = False
root.i = 0

     
def openFile(): 
    try:
        root.songAdded = True
        root.filename = filedialog.askopenfilename(initialdir = "/",
        title = "Select your track",filetypes = (("mp3 Files","*.mp3"),("m4a Files","*.m4a")))
        root.playlist.append(root.filename)
        print(" Added: " + root.filename)
        root.screenMessage.set("Press Play")
    except:
        print("Couldn't load music")








def playMusic():
    if(root.songAdded == False):
        root.screenMessage.set("Add music with 'Open File'")
    else:
        try:
            if(root.pauseFlag == True):
                pygame.mixer.music.unpause()
            else:
                print("Playing")
                pygame.mixer.init()
                pygame.mixer.music.load(root.playlist[root.i])
                pygame.mixer.music.play()
                root.screenMessage.set("Playing " + root.playlist[root.i])
        except:
            print("Couldn't play music")












def pauseMusic():
    if(root.songAdded == False):
        root.screenMessage.set("Add music with 'Open File'")
    else:
        try:
            pygame.mixer.music.pause()
            root.pauseFlag = True
            root.screenMessage.set("Paused")
        except:
            print("Couldn't pause")

def stopMusic():
    if(root.songAdded == False):
        root.screenMessage.set("Add music with 'Open File'")
    else:
        pygame.mixer.music.fadeout(600)
        root.screenMessage.set("End of Playback")

def prevMusic():
    if(root.songAdded == False):
        root.screenMessage.set("Add music with 'Open File'")
    else:
        try:
            if(root.playlist[root.i - 1]):
                root.i -= 1
                playMusic()
            else:
                print("No previous songs")
                root.screenMessage.set("No previous songs")
        except:
            stopMusic()
            print("No previous songs")













def nextMusic():
    if(root.songAdded == False):
        root.screenMessage.set("Add music with 'Open File'")
    else:
        try:

            if(root.playlist[root.i]):
                root.i += 1
                playMusic()
            else:
                root.i -= 1
        except:
            root.screenMessage.set("End of Playback.")










    
          

#---------Creating Menus----------
menu.add_cascade(label="Open File", command=openFile)
menu.add_cascade(label="Exit", command=lambda: root.destroy())
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


#---------Player Buttons----------

button1 = Button(topFrame, text="Previous",
fg="#FF00FF", command=prevMusic)
button1.pack(side=LEFT,padx=5,pady=20)
button2 = Button(topFrame, text="Play",fg="green", command=playMusic)
button2.pack(side=LEFT,padx=5,pady=20)
button3 = Button(topFrame, text="Pause",fg="black", command=pauseMusic)
button3.pack(side=LEFT,padx=5,pady=20)
button5 = Button(topFrame, text="Stop",fg="red", command=stopMusic)
button5.pack(side=LEFT,padx=5,pady=20)
button4 = Button(topFrame, text="Next",fg="blue", command=nextMusic)
button4.pack(side=LEFT,padx=5,pady=20)


#-----------The status Bar--------------
root.screenMessage = StringVar()
label = Message( root, textvariable=root.screenMessage, relief=RAISED )
root.screenMessage.set("             Hello")
label.pack(side=BOTTOM,fill=BOTH,padx=2)
root.mainloop()#refreshing the window so that it stays on the screen
