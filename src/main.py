import lib.make as make

left = make.smallmotor(1)
right = make.smallmotor(2)
train = make.drivetrain(left, right)

while True:
    train.drive(100, 1)
    train.turn(100, 1)
    train.curve(100, 50, 1)
    make.wait()

# import board
# import digitalio
# import time
# import pwmio
# # from adafruit_motor import servo, motor
# import adafruit_motor

# digout = digitalio.DigitalInOut(board.GP25)
# digout.direction = digitalio.Direction.OUTPUT

# while True:
#     digout.value ^= True
#     time.sleep(1)
