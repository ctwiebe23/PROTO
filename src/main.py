import lib.make as make

left = make.smallmotor(10)
right = make.smallmotor(13, -1)

d = make.drivetrain(left, right)

up = make.button(8)
down = make.button(9)

while True:
    make.wait()
    
    if up.pressed():
        d.drive(100, 5)
    elif down.pressed():
        d.drive(50, 5)
