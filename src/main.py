import make                          # start the code

onbutton  = make.button(1)           # on button on port 1
offbutton = make.button(2)           # off button on port 2
dcmotor   = make.largemotor(7)       # large motor on port 7

make.until(onbutton.pressed)         # pause until the on button is pressed
dcmotor.spin(50, 1.5)                # spin the dc at 50% speed for 1.5 seconds

# loop for as long as both on and off aren't pressed at once
while not (onbutton.pressed() and offbutton.pressed()):

    if onbutton.pressed():           # if the on button is pressed,
        dcmotor.spin(-50)            # spin the dc at 50% speed backwards

    if offbutton.pressed():          # if the off button is pressed,
        dcmotor.stop()               # stop the dc

    make.pause()                     # pause for a very, very short time
