import board
import pwmio
from adafruit_motor import servo
from proto.general.constants import FRQ, GROVE_PORTS
from proto.general.functions import wait, sig_int, bound_power

SERVO_PORTS = {
    10: (board.GP12, None),
    11: (board.GP13, None),
    12: (board.GP14, None),
    13: (board.GP15, None),
}

SERVO_PORTS.update( GROVE_PORTS )

SERVO_THROTTLE_RANGE = (0.1, 1)

class smallmotor:
    "A small motor plugged into a small motor port or GROVE port."

    def __init__( self, port: int, direction: int = 1 ):
        self.__io = servo.ContinuousServo(
            pwmio.PWMOut(
                SERVO_PORTS[port][0],
                frequency = FRQ,
            )
        )
        self.__direction = sig_int( direction )

    def spin( self, power: float, seconds: float = None ) -> None:
        """
        Spin the small motor at the given power for the given time period; if
        no period is given then it spins until stopped.
        """
        self.__io.throttle = self.__direction * bound_power(
            power,
            SERVO_THROTTLE_RANGE,
        )

        if seconds != None:
            wait( seconds )
            self.stop()

    def stop( self ) -> None:
        "Stops the small motor."
        self.spin( 0 )
