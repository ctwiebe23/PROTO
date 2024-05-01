import make


onbutton  = make.button(1)
offbutton = make.button(2)
servo     = make.smallmotor(3)


while not (onbutton.pressed() and offbutton.pressed()):
    
    if onbutton.pressed():
        servo.spin(100)

    if offbutton.pressed():
        servo.spin(-100)
        
    make.pause()

servo.stop()