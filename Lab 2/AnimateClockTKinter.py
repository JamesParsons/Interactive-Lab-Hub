# James Sahler Parsons
# IDD sep 2021
# Cornell Tech


# lab 2, making a clock program
# sheep jumping a fence

from time import strftime, sleep, time
import time
from PIL import Image, ImageDraw
import numpy as np
from tkinter import *

#######################################################################################
def drawGround(width, height, minute):
    
    if minute >= 0 and minute < 30:
        groundhue = 120 + (minute * 4)
    else:
        midstep = minute - 30
        groundhue = 240 - (midstep * 4)
        
    
    hexcolor = "#%02x%02x%02x" % (0, groundhue, 0) 
         
    tre = 0  

    print(width, height)
    canvas.create_rectangle(0,tre,width,height, outline=None, fill=hexcolor)

#####################################################################################

currentMin = int(time.localtime().tm_min)
currentHour = int(time.localtime().tm_hour)

#####################################################################

# make the root window
root = Tk()
root.title("Time to Sheep")

#getting screen width and height of display
screenwidth= root.winfo_screenwidth() 
screenheight= root.winfo_screenheight()

newwidth = screenwidth
newheight = screenheight
    
if screenheight * 2.5 > screenwidth:
    #print("part 1 is happening")
    newheight = screenwidth * .4
else:
    newwidth = screenheight * 2.5
    #print("part 2 is happening")
    
root.geometry("%dx%d" % (newwidth, newheight))

    
print("newwidth: ", newwidth, " newheight ", newheight)
#height = newwidth
#width = newheight

canvas = Canvas(root)
#canvas.place(x=newwidth, y=newheight)
canvas.pack()
     
drawGround(newwidth, newheight, 5)
canvas.update()    

sheep = canvas.create_rectangle(0,0,100,100,fill="#0022FF")
canvas.update()
sleep(2)
canvas.move(sheep, 250,250)
#canvas.update()
     
mainloop()
        

#######################################################################################


























## make the root window
#root = Tk()
#root.title("Time to Sheep")
##setting tkinter window size
#root.geometry("%dx%d" % (width, height))

##getting screen width and height of display
#screenwidth= root.winfo_screenwidth() 
#screenheight= root.winfo_screenheight()

#if (screenwidth / screenheight) < 2.5:
    #newwidth = ((screenheight*5)/2)

#canvas = Canvas(root)
#canvas.place(x=(screenwidth*.1),y=(screenheight*.1))
#canvas.create_oval(10, 10, 200, 200, width=2, fill='blue')
#canvas.pack()
#sleep(3)
#canvas.create_oval(10, 10, 200, 200, width=2, fill='red')
#canvas.update()
#sleep(3)
#canvas.create_oval(10, 10, 200, 200, width=2, fill='blue')
#canvas.update()
     
#mainloop()

#canvas.create_oval(10, 10, 200, 200, width=2, fill='blue')
#canvas.pack()
#sleep(3)
#canvas.create_oval(10, 10, 200, 200, width=2, fill='red')
#canvas.update()
#sleep(3)
#canvas.create_oval(10, 10, 200, 200, width=2, fill='blue')
#canvas.update()










#for x in range(120,240,20):
    #hex = "#%02x%02x%02x" % (0, x, 0) 
    #print(hex)




    # width=135,
    # height=240,
    # x_offset=53,
    # y_offset=40,
    
#width=240
#height=135
#x_offset=53
#y_offset=40    

#width = 2000
#height = 800
    
#width = 240
#height = 135


#xsheep = (width * .025)
#ysheep = (height * .6875)
#xfence = (width * .05)
#yfence = (height * .625)
#groundLevel = (height * .75)
#stopper = 1








## https://www.geeksforgeeks.org/how-to-create-full-screen-window-in-tkinter/
