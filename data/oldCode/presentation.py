import make

right  = make.button(1)

moterA = make.smallmotor(3)
moterB = make.smallmotor(4)
robot  = make.drivetrain(moterA, moterB)

speed  = 50

def Forward():
  robot.drive(speed, 2)

while True:
  if right.pressed():
    Forward()
