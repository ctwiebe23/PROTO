import lib.make as make

# vocab:
#     make.largemotor & make.smallmotor:
#         spin()
#         stop()
#         make.reversed
#     make.drivetrain:
#         drive()
#         turn()
#         curve()
#         stop()
#         make.reversed
#     make.button:
#         pressed()
#     make.wait()
#     make.wait_until()

# naming
stopbutton = make.button(2)
leftwheel = make.largemotor(7)
rightwheel = make.largemotor(8)
myrobot = make.drivetrain(leftwheel, rightwheel)
arm = make.smallmotor(6, make.reversed)

# actions
myrobot.drive(speed=40, seconds=4)
myrobot.turn(speed=30, seconds=2)
myrobot.curve(left_speed=60, right_speed=90, seconds=2.5)
arm.spin(speed=-100, seconds=1.7)
arm.spin(speed=100, seconds=1.7)

# code is read top to bottom
make.wait(seconds=2)
rightwheel.spin(speed=100, seconds=3)
myrobot.turn(speed=-30)
make.wait_until(stopbutton.pressed)
myrobot.stop()
