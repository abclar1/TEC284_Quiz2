from gpiozero import LED, Button

redButton = Button(4)
greenButton = Button(17)
blueButton = Button(27)
redLight = LED(16)
greenLight = LED(20)
blueLight = LED(21)

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
            
            
while True:
    controlLights()

