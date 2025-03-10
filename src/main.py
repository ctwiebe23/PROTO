import lib.make as make

# naming 

left_motor = make.largemotor(7)
right_motor = make.largemotor(6)

# actions

left_motor.spin(100)
right_motor.spin(100)

make.wait(2)
left_motor.spin(0)
right_motor.spin(0)

# learn2code-proto.github.io

# coin pick-up
# minefield