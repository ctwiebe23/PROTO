# exports
from proto.general.constants    import reversed
from proto.general.functions    import wait, wait_until

from proto.motion.smallmotor    import smallmotor
from proto.motion.largemotor    import largemotor
from proto.motion.drivetrain    import drivetrain

from proto.sensors.button       import button
from proto.sensors.sonar        import sonar

from proto.feedback.led         import led_blink, led_off, led_on

# start-up script
with button( 1 ) as start_button:
    wait_until( start_button.pressed )

wait( 0.3 )
