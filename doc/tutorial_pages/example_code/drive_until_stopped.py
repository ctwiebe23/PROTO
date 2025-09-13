import make

left_motor = make.largemotor(port=6)
right_motor = make.largemotor(port=7, direction=-1)
my_robot = make.drivetrain(left_motor, right_motor)

stop_button = make.button(port=8)

my_robot.drive(100)
make.wait_until(stop_button.pressed)
my_robot.stop()
