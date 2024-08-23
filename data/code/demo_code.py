import lib.make as make

# demo code for initial presentation

# componant declaration
inc_button  = make.button( 1 )
enter       = make.button( 2 )
left_drive  = make.largemotor( 7 )
right_drive = make.largemotor( 8 )
robot       = make.drivetrain( left_drive, right_drive, drift = 0.9 )
grasp_motor = make.smallmotor( 6 )

# variable declaration
grasp_time  = 1.7
grasp_speed = 100
drive_time  = 1
drive_speed = 75

# demo functions
def drive_forward():
    robot.drive( drive_speed, drive_time )

def drive_backward():
    robot.drive( -drive_speed, drive_time )

def spin():
    robot.turn( drive_speed, drive_time )

def toggle_grasp():
    global grasp_speed
    grasp_motor.spin( grasp_speed, grasp_time )
    grasp_speed *= -1

def demo():
    drive_forward()
    spin()
    toggle_grasp()
    toggle_grasp()
    drive_backward()

# demo selection
selection = 0
programs  = {
    0: drive_forward,
    1: drive_backward,
    2: spin,
    3: toggle_grasp,
    4: demo,
}

# main loop
while True:

    if inc_button.pressed():
        selection += 1 if selection < 4 else 0
        make.wait( 0.1 )

    if enter.pressed():
        programs[selection]()
        selection = 0

    make.wait()
