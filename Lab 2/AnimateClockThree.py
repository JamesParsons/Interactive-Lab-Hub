# James Sahler Parsons
# IDD sep 2021
# Cornell Tech


# lab 2, making a clock program
# sheep jumping a fence

from time import strftime, sleep, time
#from time import *
from PIL import Image, ImageDraw
from tkinter import *

########################################################################################

######################################################################################
    
#######################################################################################
def drawGround(width, height, minute):
    
    # want the grass to get brighter green then darker again
    if minute >= 0 and minute < 30:
        groundhue = 120 + (minute * 4)
    else:
        midstep = minute - 30
        groundhue = 240 - (midstep * 4)
           
    hexcolor = "#%02x%02x%02x" % (0, groundhue, 0)       
    canvas.create_rectangle(0,(height * .75),width, height,outline=None, fill=hexcolor)
  
######################################################################################

currentMin = int(time.localtime().tm_min)
currentHour = int(time.localtime().tm_hour)

#####################################################################

# make the root window
root = Tk()
root.state('zoomed')

#getting screen width and height of display
screenwidth= root.winfo_screenwidth() 
screenheight= root.winfo_screenheight()

newwidth = screenwidth
newheight = screenheight

# trying to keep it consistent 2.5:1 ratio  
if screenheight * 2.5 > screenwidth:
    newheight = screenwidth * .4
else:
    newwidth = screenheight * 2.5
    
canvas = Canvas(root, width=newwidth, height=newheight)
canvas.pack()

width = newwidth
height = newheight
####################################################################################################


######################################### Sky ######################################################

# draw original objects
canvas.create_rectangle(0,0,newwidth,newheight,fill="#00CDFF")
ground = canvas.create_rectangle(0,(height * .75),width, height,outline=None, fill="#00FF3C")
sun = canvas.create_oval(width*.85,height*-.25,width*1.15,height*.25,fill="#FFFF00")
sheep = canvas.create_rectangle((width*.1),(height*.6),(width*.2),(height*.72), outline="#000000", fill="#FFFFFF")
fence = canvas.create_rectangle((width*.95),(height*.68),(width*.97),(height*.75),fill="#734B0F")
canvas.update()
     
stopper = 1   
#runs the clock
while True:
    
    # time
    sectime = int(time.localtime().tm_sec)
    mintime = int(time.localtime().tm_min)
    hrtime = int(time.localtime().tm_hour) 
 
    canvas.move(fence, -100,0)
 
    #canvas.update()  
    stopper = stopper + 1
    
canvas.move(fence, -100,0)
sleep(3)
canvas.move(fence, -100,0)
sleep(3)
canvas.move(fence, -100,0)
sleep(3)
canvas.move(fence, -100,0)
sleep(3)
canvas.move(fence, -100,0)
sleep(3)
canvas.move(fence, -100,0)
sleep(1)
canvas.move(fence, -100,0)
sleep(1)
canvas.move(fence, -100,0)
    
mainloop()











####################################################################################################
def moveLeg():
    canvas.move(ul,width*.5,height*.5)








