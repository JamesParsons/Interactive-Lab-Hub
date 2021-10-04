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

########################################################################################
#def drawGround(width, height, minute):
    
    #if minute >= 0 and minute < 30:
        #groundhue = 120 + (minute * 4)
    #else:
        #midstep = minute - 30
        #groundhue = 240 - (midstep * 4)
        
    
    #hexcolor = "#%02x%02x%02x" % (0, groundhue, 0) 
         
    #canvas.create_rectangle(0,0,width, height,fill=hexcolor)

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

#####################################################################################
#def drawSheep(width, height, second):
    
    ## format is xstart = start x position.   xend = start position + thickness
    #thickness = width * .03
    #offset1 = (width * .0125)
    
    ## y+ goes down, x+ goes right
    #sheep = (canvas.create_rectangle((width*.1125),(height*.63)+thickness,(width*.125),(height*.75), outline="#000000", fill="#FFFFFF"),
             #canvas.create_rectangle((width*.1375),(height*.63)+thickness,(width*.15),(height*.75), outline="#000000", fill="#FFFFFF"),
             #canvas.create_oval((width * .1),(height * .65),(width * .1) + thickness,(height * .65) + thickness, outline=None,fill="#FFFFFF"), # LL
             #canvas.create_oval((width * .1125),(height * .64),(width * .1125) + thickness,(height * .64) + thickness, outline=None,fill="#FFFFFF"), #LM
             #canvas.create_oval((width * .125),(height * .65),(width * .125) + thickness,(height * .65) + thickness, outline=None,fill="#FFFFFF"), #LR
             #canvas.create_oval((width * .1),(height * .60),(width * .1) + thickness,(height * .60) + thickness, outline=None,fill="#FFFFFF"), #UL
             #canvas.create_oval((width * .1125),(height * .59),(width * .1125) + thickness,(height * .59) + thickness, outline=None,fill="#FFFFFF"), #UM
             #canvas.create_oval((width * .125),(height * .60),(width * .125) + thickness,(height * .60) + thickness, outline=None,fill="#FFFFFF"), #UR
             #canvas.create_oval((width * .14),(height * .57),(width * .14) + thickness,(height * .57) + thickness, outline=None,fill="#FFFFFF"))
   
    #canvas.update()
  
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

print(screenwidth, screenheight)

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
def moveLeg():
    canvas.move(ul,width*.5,height*.5)

######################################### Sky ######################################################

#sky
canvas.create_rectangle(0,0,newwidth,newheight,fill="#00CDFF")
canvas.update()

############################################### Ground ############################################

ground = canvas.create_rectangle(0,(height * .75),width, height,outline=None, fill="#00FF3C")

##################################### Sun #######################################################

sun = canvas.create_oval(width*.85,height*-.25,width*1.15,height*.25,fill="#FFFF00")

############################################# Sheep Parts ########################################
thickness = width * .03
offset1 = (width * .0125)

# y+ goes down, x+ goes right
backleg = canvas.create_rectangle((width*.1125),(height*.63)+thickness,(width*.125),(height*.75), outline="#000000", fill="#FFFFFF")
frontleg = canvas.create_rectangle((width*.1375),(height*.63)+thickness,(width*.15),(height*.75), outline="#000000", fill="#FFFFFF")
ul =canvas.create_oval((width * .1),(height * .65),(width * .1) + thickness,(height * .65) + thickness, outline=None,fill="#FFFFFF") # LL
um = canvas.create_oval((width * .1125),(height * .64),(width * .1125) + thickness,(height * .64) + thickness, outline=None,fill="#FFFFFF") #LM
ul = canvas.create_oval((width * .125),(height * .65),(width * .125) + thickness,(height * .65) + thickness, outline=None,fill="#FFFFFF") #LR
ll = canvas.create_oval((width * .1),(height * .60),(width * .1) + thickness,(height * .60) + thickness, outline=None,fill="#FFFFFF") #UL
lm = canvas.create_oval((width * .1125),(height * .59),(width * .1125) + thickness,(height * .59) + thickness, outline=None,fill="#FFFFFF") #UM
lr = canvas.create_oval((width * .125),(height * .60),(width * .125) + thickness,(height * .60) + thickness, outline=None,fill="#FFFFFF") #UR
head = canvas.create_oval((width * .14),(height * .57),(width * .14) + thickness,(height * .57) + thickness, outline=None,fill="#FFFFFF")
canvas.update()


########################################################################################################
     
stopper = 1   
# runs the clock
while stopper == 1:
#while True:
    
    # time
    sectime = int(time.localtime().tm_sec)
    mintime = int(time.localtime().tm_min)
    hrtime = int(time.localtime().tm_hour) 
    
    # treat seconds 31-60 as 1-30
    if sectime >= 30:
        sectime = sectime - 30
    
    sleep(1)
    #drawGround(newwidth, newheight, mintime)
    #drawSheep(newwidth, newheight,sectime)
    moveLeg()
    canvas.update()    
    
   
    
    stopper = 2
mainloop()
        

#######################################################################################






class Sheep:
    def __init__(self):
        self.height = height
        self.width = width
    
        thickness = width * .03
        offset1 = (width * .0125)
        
        # y+ goes down, x+ goes right
        sheep = (canvas.create_rectangle((width*.1125),(height*.63)+thickness,(width*.125),(height*.75), outline="#000000", fill="#FFFFFF"),
                 canvas.create_rectangle((width*.1375),(height*.63)+thickness,(width*.15),(height*.75), outline="#000000", fill="#FFFFFF"),
                 canvas.create_oval((width * .1),(height * .65),(width * .1) + thickness,(height * .65) + thickness, outline=None,fill="#FFFFFF"), # LL
                 canvas.create_oval((width * .1125),(height * .64),(width * .1125) + thickness,(height * .64) + thickness, outline=None,fill="#FFFFFF"), #LM
                 canvas.create_oval((width * .125),(height * .65),(width * .125) + thickness,(height * .65) + thickness, outline=None,fill="#FFFFFF"), #LR
                 canvas.create_oval((width * .1),(height * .60),(width * .1) + thickness,(height * .60) + thickness, outline=None,fill="#FFFFFF"), #UL
                 canvas.create_oval((width * .1125),(height * .59),(width * .1125) + thickness,(height * .59) + thickness, outline=None,fill="#FFFFFF"), #UM
                 canvas.create_oval((width * .125),(height * .60),(width * .125) + thickness,(height * .60) + thickness, outline=None,fill="#FFFFFF"), #UR
                 canvas.create_oval((width * .14),(height * .57),(width * .14) + thickness,(height * .57) + thickness, outline=None,fill="#FFFFFF"))
        


