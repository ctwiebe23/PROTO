import make

on_button = make.button(1)
off_button = make.button(2)

motor = make.motor(7)

make.pause_until(on_button.is_pressed)

while not off_button.is_pressed():
    motor.spin(50)
