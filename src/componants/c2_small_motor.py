import board
import pwmio
import math
from adafruit_motor import servo
from a2_functions import *
from a1_core import *

__SERVO_PIN = {
    3: (board.GP12, None),
    4: (board.GP13, None),
    5: (board.GP14, None),
    6: (board.GP15, None),
}

__SERVO_PIN.update(GROVE_PIN)

class small_motor:
    "A small motor plugged into a small motor port or GROVE port."

    def __init__( self, pinset: int, direction: int = 1 ):
        self.__io = servo.ContinuousServo( pwmio.PWMOut(
            __SERVO_PIN[pinset][0],
            frequency = FRQ
        ))
        self.__direction = math.copysign( 1, direction )

    def spin( self, speed: float, seconds: float = None ) -> None:
        """
        Spin the small motor at the given speed for the given time period; if
        no period is given then it spins until stopped.
        """
        speed = 100 if speed > 100 else -100 if speed < -100 else speed
        self.__io.throttle = speed / 100 * self.__direction
        if seconds != None:
            pause( seconds )
            self.stop()

    def stop( self ) -> None:
        "Stops the small motor."
        self.spin( 0 )
