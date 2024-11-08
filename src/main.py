import lib.make as make

button = make.button( port=9 )
motor = make.largemotor( port=6 )

if button.pressed():
  motor.spin( power=100 )
  make.wait( seconds=1 )
  while not button.pressed():
    make.wait()
else:
  motor.spin( power=100, seconds=5 )
