import make

left = make.largemotor(6)
right = make.largemotor(7)
dt = make.drivetrain(left, right, drift=10/8)

# cservo = make.smallmotor(2)
# cservo.spin(100)

start = make.button(8)
stop = make.button(9)

dt.drive(100)

while True:
  if start.pressed():
    dt.drive(100)
  if stop.pressed():
    dt.stop()
  make.wait()
