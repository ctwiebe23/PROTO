# exports
import proto.system as system

from proto.general.functions import wait, wait_until, wait_while

from proto.motion.smallmotor import smallmotor
from proto.motion.largemotor import largemotor
from proto.motion.drivetrain import drivetrain
from proto.motion.servo import servo

from proto.input.button import button

# start-up script
with button(8) as start_button:
    wait_until(start_button.pressed)
    wait(1)
