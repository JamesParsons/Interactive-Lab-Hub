#Import the library
from tkinter import *
from time import time,sleep


#Create an instance of tkinter frame
root= Tk()
root.state('zoomed')

#Define the geometry of window
#rootWindow.geometry("600x400")

#Create a canvas object
canvas= Canvas(root,width=400, height=400)
canvas.pack()

#Draw an Oval in the canvas
oval = canvas.create_oval(60,60,210,210)
oval2 = canvas.create_oval(80,80,210,210)
  
canvas.update()

sleep(2)
canvas.move(oval,100,100)

mainloop()

