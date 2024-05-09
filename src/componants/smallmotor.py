import board
import pwmio
from adafruit_motor import servo
from base import *
from functions import *

class smallmotor:
    "An object representing a servo"

    SERVO_PIN = {
        3: (board.GP12, None),
        4: (board.GP13, None),
        5: (board.GP14, None),
        6: (board.GP15, None),
    }
    
    SERVO_PIN.update(GROVE_PIN)
    
    def __init__( self, pinset: int, direction: int = 1 ):
        self.io = servo.ContinuousServo( pwmio.PWMOut(
            self.SERVO_PIN[pinset][0],
            frequency = FRQ
        ))
        self.direction = direction

    def spin( self, speed: float, seconds: float = None ) -> None:
        "Spin the servo at the given speed"
        speed = 100 if speed > 100 else -100 if speed < -100 else speed
        self.io.throttle = speed / 100 * self.direction
        if seconds != None:
            pause( seconds )
            self.io.throttle = 0

    def stop( self ) -> None:
        "Stops the motor"
        self.spin( 0 )
