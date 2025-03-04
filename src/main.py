import lib.make as make

base   = make.largemotor(6)
joint1 = make.largemotor(7)
joint2 = make.smallmotor(4)
joint3 = make.servo(5)

start = make.button(8)

def main():
    base.spin(0.25)
    joint1.spin(100)
    make.wait(2)
    base.spin(-0.25)
    joint1.spin(-100)
    make.wait(2)
    base.stop()
    joint1.stop()

    joint2.spin(100)

    for angle in range(90, 180, 5):
        joint3.moveto(angle)
        make.wait(0.3)

    joint2.stop()

main()

while True:
    if start.pressed():
        main()
    make.wait()
