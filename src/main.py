from lib.make import *

stop_button = button(1)
robot       = drivetrain(largemotor(7), largemotor(8))
arm         = smallmotor(6)

arm.spin(1)
wait_until(stop_button.pressed)
