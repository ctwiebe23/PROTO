import lib.make as make


counter    = make.button(1)
enter      = make.button(2)

leftDrive  = make.largemotor(7)
rightDrive = make.largemotor(8, make.reversed)
robot      = make.drivetrain(leftDrive, rightDrive)

grasp      = make.smallmotor(6)
gTime      = 1
gSign      = 1


def driveForward():
  robot.drive(25, 2)

def spin():
  robot.turn(25, 2)
      
def toggleGrasp():
  global gSign, gTime
  grasp.spin(25 * gSign, gTime)
  gSign *= -1


programs = {
  0: driveForward,
  1: spin,
  2: toggleGrasp,
}

selection = 0


while True:
  
  if counter.pressed():
    selection += 1 if selection < 2 else 0
    make.pause(0.1)
  
  if enter.pressed():
    programs[selection]()
    selection = 0
  
  make.pause()