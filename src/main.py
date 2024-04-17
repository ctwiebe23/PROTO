import make

on_button  = make.button(1)
off_button = make.button(2)
motor = make.largemotor(7)

make.until(on_button.pressed)

motor.spin(-50)
make.pause(1.5)
motor.spin(0)

while not (on_button.pressed() and off_button.pressed()):
    if on_button.pressed():
        motor.spin(50)
    if off_button.pressed():
        motor.spin(0)
    make.pause()
