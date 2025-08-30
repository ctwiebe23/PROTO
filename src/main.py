from lib.make import *

left = largemotor(6)
right = largemotor(7, direction=-1)
bot = drivetrain(left, right)

stop = button(9)

bot.drive(100)
wait_until(stop.pressed)
bot.stop()
