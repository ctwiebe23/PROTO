# exports
from proto.general.constants    import reversed
from proto.general.functions    import wait, wait_until

from proto.motion.smallmotor    import smallmotor
from proto.motion.largemotor    import largemotor
from proto.motion.drivetrain    import drivetrain

from proto.sensors.button       import button

# start-up script
wait_until(button(1).pressed)
