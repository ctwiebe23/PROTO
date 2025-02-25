import lib.make as make

# naming components
left    = make.largemotor(6)
right   = make.largemotor(7)
bot     = make.drivetrain(left, right, drift=10/8)

start   = make.button(8)
stop    = make.button(9)

arm     = make.servo(2)

# taking actions
for angle in range(180, 0, -30):
    arm.moveto(angle)
    make.wait(0.5)

bot.turn(100)

while not stop.pressed():
    pass
