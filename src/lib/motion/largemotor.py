import board
import pwmio
import math
from adafruit_motor import motor
from general.constants import FRQ
from general.functions import wait

DC_PORTS = {
    7: (board.GP8,  board.GP9),
    8: (board.GP10, board.GP11),
}

class largemotor:
    "A large motor plugged in to a large motor port."

    def __init__( self, port: int, direction: int = 1 ):
        forward   = pwmio.PWMOut( DC_PORTS[port][0], frequency = FRQ )
        backward  = pwmio.PWMOut( DC_PORTS[port][1], frequency = FRQ )
        self.__io = motor.DCMotor( forward, backward )
        self.__direction = math.copysign( 1, direction )

    def spin( self, speed: float, seconds: float = None ) -> None:
        """
        Spin the large motor at the given speed for the given time period; if
        no period is given then it spins until stopped.
        """
        speed = 100 if speed > 100 else -100 if speed < -100 else speed
        self.__io.throttle = speed / 100 * self.__direction
        if seconds != None:
            wait( seconds )
            self.stop()

    def stop( self ) -> None:
        "Stops the large motor."
        self.spin( 0 )
