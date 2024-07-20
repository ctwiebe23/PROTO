import lib.make as make

# demo code for initial presentation

# componant declaration
inc_button  = make.button( 1 )
enter       = make.button( 2 )
left_drive  = make.large_motor( 7 )
right_drive = make.large_motor( 8 )
robot       = make.wagon( left_drive, right_drive, drift = 0.9 )
grasp_motor = make.small_motor( 6 )

# variable declaration
graspTime  = 1.7
graspSpeed = 100
driveTime  = 1
driveSpeed = 75

# demo functions
def driveForward():
  robot.drive( driveSpeed, driveTime )

def driveBackward():
  robot.drive( -driveSpeed, driveTime )

def spin():
  robot.turn( driveSpeed, driveTime )

def toggleGrasp():
  global graspSpeed
  grasp_motor.spin( graspSpeed, graspTime )
  graspSpeed *= -1

def demo():
  driveForward()
  spin()
  toggleGrasp()
  toggleGrasp()
  driveBackward()

# demo selection
selection = 0
programs  = {
  0: driveForward,
  1: driveBackward,
  2: spin,
  3: toggleGrasp,
  4: demo,
}

# main loop
while True:

  if inc_button.pressed():
    selection += 1 if selection < 4 else 0
    make.pause( 0.1 )

  if enter.pressed():
    programs[selection]()
    selection = 0

  make.pause()
