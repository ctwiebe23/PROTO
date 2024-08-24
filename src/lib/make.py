# exports
from general.constants  import reversed
from general.functions  import wait, wait_until

from motion.smallmotor  import smallmotor
from motion.largemotor  import largemotor
from motion.drivetrain  import drivetrain

from sensors.button     import button

# start-up script
wait_until(button(1).pressed)
