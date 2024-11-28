# exports
from proto.general.functions    import wait, wait_until

from proto.motion.smallmotor    import smallmotor
from proto.motion.largemotor    import largemotor
from proto.motion.drivetrain    import drivetrain

from proto.input.button         import button

# start-up script
with button( 8 ) as start_button:
    start_button.wait_until_pressed()
    wait( 1 )
