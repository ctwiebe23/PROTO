import lib.make as make

stop_button = make.button(1)
robot       = make.drivetrain(make.largemotor(7), make.largemotor(8))
arm         = make.smallmotor(6)

arm.spin(speed=10)
make.wait_until(stop_button.pressed)

robot.turn(speed=25, seconds=2)
