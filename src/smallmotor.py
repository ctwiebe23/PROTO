import board
import pwmio
from adafruit_motor import servo
from functions import *

__SERVO_PIN = {
    3: (board.GP12, None),
    4: (board.GP13, None),
    5: (board.GP14, None),
    6: (board.GP15, None),
}

__SERVO_PIN.update(__GROVE_PIN)

class smallmotor:
    "An object representing a servo"

    def __init__( self, pinset: int, direction: int = 1 ):
        self.__io = servo.ContinuousServo( pwmio.PWMOut(
            __SERVO_PIN[pinset][0],
            frequency = __FRQ
        ))
        self.__direction = direction

    def spin( self, speed: float, seconds: float = None ) -> None:
        "Spin the servo at the given speed"
        speed = 100 if speed > 100 else -100 if speed < -100 else speed
        self.__io.throttle = speed / 100 * self.__direction
        if seconds != None:
            pause( seconds )
            self.stop()

    def stop( self ) -> None:
        "Stops the motor"
        self.spin( 0 )
