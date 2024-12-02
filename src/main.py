import lib.make as make

left    = make.smallmotor(11)
right   = make.smallmotor(13, -1)

robot   = make.drivetrain(left, right)

button1 = make.button(8)
button2 = make.button(9)

while True:
        robot.drive(100)
        button2.wait_until_pressed()
        robot.stop()
        button2.wait_until_pressed()
