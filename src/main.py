from lib.make import *

stop    = button(2)
robot   = drivetrain(largemotor(7), largemotor(8))
arm     = smallmotor(6)

robot.drive(50, 2)
robot.turn(75, 1)
robot.drive(50, 2)

arm.spin(100, 1.7)
arm.spin(-100, 1.7)

robot.turn(25)
wait_until(stop.pressed)
