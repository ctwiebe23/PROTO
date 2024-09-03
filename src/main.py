from lib.make import *

kissa   = button(1)
kitty   = drivetrain(largemotor(7), largemotor(8))
cat     = smallmotor(6)

cat.spin(1)
wait_until(kissa.pressed)
