"""
Contains the public exports of MAKE.

Everything that should be exposed to the user is imported here.
"""

from proto.general.functions import wait, wait_until, wait_while

from proto.motion.smallmotor import smallmotor
from proto.motion.largemotor import largemotor
from proto.motion.drivetrain import drivetrain
from proto.motion.servo import servo

from proto.input.button import button
from proto.output.light import light

# So the user can alter system components without editing the library itself
import proto.system as system
from proto.schemata import board_schema, cservo_schema, servo_schema, motor_driver_schema

# Start-up script
builtin_light = None

if system.board.builtin_light_port != None:
    builtin_light = light(system.board.builtin_light_port)
    builtin_light.on()

if system.board.start_button_port != None:
    with button(system.board.start_button_port) as start_button:
        wait_until(start_button.pressed)

if builtin_light != None:
    builtin_light.off()
    builtin_light.free_port()
