import board
import pwmio
import math
from adafruit_motor import motor
from functions import *

__DC_PIN = {
    7: (board.GP8,  board.GP9),
    8: (board.GP10, board.GP11),
}

class largemotor:
    "An object representing a DC motor"

    def __init__( self, pinset: int, direction: int = 1 ):
        forward   = pwmio.PWMOut( __DC_PIN[pinset][0], frequency = __FRQ )
        backward  = pwmio.PWMOut( __DC_PIN[pinset][1], frequency = __FRQ )
        self.__io = motor.DCMotor( forward, backward )
        self.__direction = math.copysign( 1, direction )

    def spin( self, speed: float, seconds: float = None ) -> None:
        """
        Spin the motor at the given speed for the given time period; if no
        period is given then it spins until stopped
        """
        speed = 100 if speed > 100 else -100 if speed < -100 else speed
        self.__io.throttle = speed / 100 * self.__direction
        if seconds != None:
            pause( seconds )
            self.stop()

    def stop( self ) -> None:
        "Stops the motor"
        self.spin( 0 )
