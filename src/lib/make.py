"""
Contains the public exports of MAKE.

Everything that should be exposed to the user is imported here.
"""

# So the user can alter system components without editing the library itself
import proto.system as system

from proto.general.functions import wait, wait_until, wait_while

from proto.motion.smallmotor import smallmotor
from proto.motion.largemotor import largemotor
from proto.motion.drivetrain import drivetrain
from proto.motion.servo import servo

from proto.input.button import button

# Start-up script
with button(8) as start_button:
    wait_until(start_button.pressed)
    wait(1)
