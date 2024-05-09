import board
import pwmio
from adafruit_motor import motor
from alpha import *
from functions import *

class largemotor:
    "An object representing a DC motor"

    DC_PIN = {
        7: (board.GP8 , board.GP9 ),
        8: (board.GP10, board.GP11),
    }

    def __init__( self, pinset: int, direction: int = 1 ):
        forward  = pwmio.PWMOut( self.DC_PIN[pinset][0], frequency = FRQ )
        backward = pwmio.PWMOut( self.DC_PIN[pinset][1], frequency = FRQ )
        self.io  = motor.DCMotor( forward, backward )
        self.direction = direction

    def spin( self, speed: float, seconds: float = None ) -> None:
        """
        Spin the motor at the given speed for the given time period; if no
        period is given then it spins until stopped
        """
        speed = 100 if speed > 100 else -100 if speed < -100 else speed
        self.io.throttle = speed / 100 * self.direction
        if seconds != None:
            pause( seconds )
            self.io.throttle = 0

    def stop( self ) -> None:
        "Stops the motor"
        self.spin( 0 )
