import make

right  = make.button(1)

motorA = make.largemotor(7)
motorE = make.largemotor(8)
robot  = make.drivetrain(motorA, motorE)

speed  = 50

def Forward():
  robot.drive(speed, 2)

while True:
  if right.pressed():
    Forward()
