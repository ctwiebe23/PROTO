import lib.make as make

stop    = make.button(2)
left    = make.largemotor(7)
right   = make.largemotor(8)
robot   = make.drivetrain(left, right)
arm     = make.smallmotor(6)

robot.drive(50, 2)
robot.turn(75, 1)
robot.drive(50, 2)

arm.spin(100, 1.7)
arm.spin(-100, 1.7)

robot.turn(25)
make.wait_until(stop.pressed)

arm.spin(50)
robot.drive(50)
make.wait(10)
arm.stop()

arm.spin(50, 2)

# while not stop.pressed():
#     arm.spin(50, 0.05)
    
# arm.spin(50)
# make.wait_until(stop.pressed)
# arm.stop()

# motor demonstration