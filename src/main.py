import lib.make as make

# name the drive motors
left    = make.smallmotor( port=11 )
right   = make.smallmotor( port=13, direction=-1 )  # this motor's facing the
                                                    #  opposite direction
# name the robot, using the motors
robot   = make.drivetrain( left_motor=left, right_motor=right )

# name the buttons
button1 = make.button( port=8 )
button2 = make.button( port=9 )

# make actions using your robot
while True:
    robot.drive( power=100 )        # no time given -- spins forever!
    button2.wait_until_pressed()    # motor still spins while the bot's waiting
    robot.stop()                    # stops the motor no matter what
    button2.wait_until_pressed()    # stays stopped while the bot's waiting
    # loops back to the `while True`
