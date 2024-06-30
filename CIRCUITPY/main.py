import lib.make as make


counter    = make.button(1)
enter      = make.button(2)

left       = make.largemotor(7)
right      = make.largemotor(8)
robot      = make.drivetrain(left, right, drift = 0.9)

grasp      = make.smallmotor(6)

graspTime  = 1.7
graspSpeed = 100
driveTime  = 1
driveSpeed = 75


def driveForward():
  robot.drive(driveSpeed, driveTime)

def driveBackward():
  robot.drive(-driveSpeed, driveTime)

def spin():
  robot.turn(driveSpeed, driveTime)

def toggleGrasp():
  global graspSpeed
  grasp.spin(graspSpeed, graspTime)
  graspSpeed *= -1

def demo():
  driveForward()
  spin()
  toggleGrasp()
  toggleGrasp()
  driveBackward()

selection = 0
programs  = {
  0: driveForward,
  1: driveBackward,
  2: spin,
  3: toggleGrasp,
  4: demo,
}


while True:

  if counter.pressed():
    selection += 1 if selection < 4 else 0
    make.pause(0.1)

  if enter.pressed():
    programs[selection]()
    selection = 0

  make.pause()
