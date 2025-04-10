#Alex Clark
#TEC 284 Quiz 2

#import the LED and Button
from gpiozero import LED, Button

#define the pins for the buttons and LED
redButton = Button(4)
greenButton = Button(17)
blueButton = Button(27)
redLight = LED(16)
greenLight = LED(20)
blueLight = LED(21)

#define a fuction to control the lights
def controlLights():
    if redButton.is_pressed:
        redLight.on()
    else:
        redLight.off()
        
    if greenButton.is_pressed:
        greenLight.on()
    else:
        greenLight.off()
        
    if blueButton.is_pressed:
        blueLight.on()
    else:
            blueLight.off()
            
#create a infinte loop then call the control lights function      
while True:
    controlLights()


