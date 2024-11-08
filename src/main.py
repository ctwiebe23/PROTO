import make

motor = make.largemotor(port=6)

motor.spin(power=50, seconds=5)
