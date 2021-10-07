import board
import digitalio
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()
int_pin = digitalio.DigitalInOut(board.D5)
apds = APDS9960(i2c, interrupt_pin=int_pin)

apds.enable_proximity = True
apds.proximity_interrupt_threshold = (0, 250)
apds.enable_proximity_interrupt = True

apds.enable_color = True
apds.enable_gesture = True

#r, g, b, c = apds.color_data
#print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))

gesture = apds.gesture()

while gesture == 0:
    gesture = apds.gesture()
print('Saw gesture: {0}'.format(gesture))


#while True:
    #print(apds.proximity)
    #apds.clear_interrupt()
    
    #r, g, b, c = apds.color_data
    #print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    
    
    
