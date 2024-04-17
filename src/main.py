import make

on_button  = make.button(1)
off_button = make.button(2)
motor = make.dc(7)

make.pause_until(on_button.is_pressed)

motor.spin(-50)
make.pause(1.5)
motor.spin(0)

while not (on_button.is_pressed() and off_button.is_pressed()):
    if on_button.is_pressed():
        motor.spin(50)
    if off_button.is_pressed():
        motor.spin(0)
    make.pause()
