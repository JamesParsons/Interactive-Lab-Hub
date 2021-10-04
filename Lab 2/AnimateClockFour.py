# James Sahler Parsons
# IDD sep 2021
# Cornell Tech


# lab 2, making a clock program
# sheep jumping a fence

from time import strftime, sleep, time
from PIL import Image, ImageDraw
from tkinter import *

########################################################################################

######################################################################################
    
#######################################################################################


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


######################################### Sky ######################################################

# draw original objects

fence = canvas.create_rectangle((width*.95),(height*.68),(width*.97),(height*.75),fill="#734B0F")
canvas.update()

for x in range(10):
    print("hi")
    
    #sleep(1)
    
    canvas.move(fence, -100,0)
     

    
mainloop()














