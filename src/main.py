from lib.make import *

arm = smallmotor(1)
hand = servo(2)

left = largemotor(6)
right = largemotor(7)

start_button = button(8)
stop_button = button(9)

bot = drivetrain(left, right, 1/1)

arm.spin(100)
wait_until(stop_button.pressed)
arm.stop()
wait(1)
arm.spin(-100, 2)

hand.moveto(0)
wait(2)
hand.moveto(90)
wait(2)
hand.moveto(180)

wait(2)

hand.moveto(0, 2)
hand.moveto(90, 2)
hand.moveto(180, 2)

wait_until(start_button.pressed)

bot.turn(100)
wait(1)
bot.turn(-100, 1)
bot.stop()

wait(1)

bot.drive(100, 2)
bot.curve(60, -20, 4)
bot.curve(40, 60, 2)

wait_until(start_button.pressed)
bot.drive(100)
wait_until(stop_button.pressed)

# activity ideas:
#   coin pick-up
#   minefield
