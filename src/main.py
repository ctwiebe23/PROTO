import lib.make as make

# The base of the crane
base = make.servo(port=1)

# The pulley
pulley = make.largemotor(port=7)

# Rotate crane to 80 degrees
base.moveto(angle=80, seconds=1)

# Lower pulley and raise it back up
pulley.spin(power=100, seconds=2)
pulley.spin_back(power=100, seconds=2)
