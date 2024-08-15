import board
import pwmio
import math
from adafruit_motor import servo
from c0_core import FRQ, GROVE_PORTS, pause

__SERVO_PORTS = {
    3: (board.GP12, None),
    4: (board.GP13, None),
    5: (board.GP14, None),
    6: (board.GP15, None),
}

__SERVO_PORTS.update(GROVE_PORTS)

class small_motor:
    "A small motor plugged into a small motor port or GROVE port."

    def __init__( self, port: int, direction: int = 1 ):
        self.__io = servo.ContinuousServo( pwmio.PWMOut(
            __SERVO_PORTS[port][0],
            frequency = FRQ
        ))
        self.__direction = math.copysign( 1, direction )

    def spin( self, speed: float, time: float = None ) -> None:
        """
        Spin the small motor at the given speed for the given time period; if
        no period is given then it spins until stopped.
        """
        speed = 100 if speed > 100 else -100 if speed < -100 else speed
        self.__io.throttle = speed / 100 * self.__direction
        if time != None:
            pause( time )
            self.stop()

    def stop( self ) -> None:
        "Stops the small motor."
        self.spin( 0 )
