# This library is use to create GUI for desktop applicationx
from tkinter import *

# Window : serves as a container to hold or contain widgets
# Widgets : there are buttons, textboxes , lables, etc.

window = Tk()   # instanciate an instance of a window

window.geometry("1080x1080")

window.title("One page")

icon = PhotoImage('diff.png')

window.iconphoto(True,icon)

window.config(background='black')

window.mainloop()       # place window on screen, listen for events
