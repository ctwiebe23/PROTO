from lib.make import *

drive_motor   = largemotor(7)
start_button  = button(8)
stop_button   = button(9)

drive_motor.spin(100, 3)

while not stop_button.pressed():
    if start_button.pressed():
        drive_motor.spin(100, 3)
    wait()
