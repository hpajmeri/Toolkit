from tkinter import *
import tkinter.messagebox as tkm
import sys;import os; 
cwd = os.getcwd()

#setting the root
root= Tk(); root.configure(background="black")
root.title("Toolkit proto1") #Sets the title
root.geometry("300x70")


#TopMenu   
m= Menu(root)
root.config(menu=m)
m.add_cascade(label="About",
command=lambda: tkm.showinfo('About Toolkit proto1',
'Our Grade 12 final project\n\nCredits:\n\nDJ Oamen (Youtube)\nneerajnabar (Github)\nDhananjayTrivedi (Github)\ndebasishbai (Github)\nChristian Thompson (Youtube)'))

m.add_cascade(label="Exit", command=root.destroy)

#status bar
status = Label(root, text="- Created by Maadhyam , Rahul and Het -",
bd=3, relief=SUNKEN, anchor=W)

status.pack(side=BOTTOM, fill=X)




#_________________________Core Code workspace start_______________


#FrameMenu
m2= Menubutton(root, text="Select from a list of tools >",
bg='#111111', fg='white',height=100,bd=9, relief=RIDGE)

m2.menu= Menu(m2)
m2["menu"] = m2.menu

m2.menu.add_command(label="Scientific Calculator            >>",command=lambda: os.system("ZCalculator.py"))
m2.menu.add_command(label="Universal Unit Convertor    >>",command=lambda: os.system("ZUnitConvertGUI.py"))

m2.menu.add_command(label="Music Player                        >>",command=lambda: os.system("ZMusicPlayer.py"))
m2.menu.add_command(label="Password Generator           >>",command=lambda: os.system("ZPass.py"))
m2.menu.add_separator()
m2.menu.add_command(label="Game: Rock,paper and scissors     >>",command=lambda: os.system("Zrps.py"))
m2.menu.add_command(label="Suggestion/Complaint system        >>",command=lambda: os.system("Zmain.py"))
m2.menu.add_command(label="To-Do List maker       >>",command=lambda: os.system("Ztodo.py"))
m2.menu.add_command(label="Formal Letter Auto Writer       >>",command=lambda: os.system("ZAutoWriter.py"))

m2.pack()

#______________________Core code workspace end_____________________________________________________________________________________



#end statement, to keep the program running       
root.mainloop()
