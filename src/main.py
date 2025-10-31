import lib.make as make

base_motor = make.servo(1)
pulley_motor = make.largemotor(7)

# Rotate crane to 80 degrees
base_motor.moveto(80, 1)

# Lower pulley and raise it back up
pulley_motor.spin(100, 2)
pulley_motor.spin_back(100, 2)
