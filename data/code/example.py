import make

stop = make.button(2)

left_motor = make.large_motor(7)
right_motor = make.large_motor(8, make.reversed)

arm = make.small_motor(6)

robot = make.drivetrain(left_motor, right_motor)

while not stop.pressed():
    robot.curve(80, 100, 4)
    
    robot.drive(40, 2)
    
    robot.turn(60)
    make.pause(1)
    robot.stop()
    
    arm.spin(20, 1)
    arm.spin(-20, 1)
    
    # go back to the start of the loop