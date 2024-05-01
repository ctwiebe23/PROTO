import board
import digitalio
import time
import pwmio
from adafruit_motor import motor, servo

"""
Carston Wiebe
carstonwiebe17@gmail.com

CIRCUITPYTHON code to test the Maker PI RP2040 with servos and dc motors
"""

reversed = -1  # for reversing servos and dc motors

CYCLE = 2 ** 15
FRQ   = 50

GROVE_PIN = {
    9:  (board.GP2 , board.GP3 ),
    10: (board.GP4 , board.GP5 ),
    11: (board.GP16, board.GP17),
    12: (board.GP6 , board.GP26),
    13: (board.GP26, board.GP27),
}

largemotors = []
smallmotors = []


class button:
    "An object representing a button"

    BUTTON_PIN = {
        1: board.GP20,
        2: board.GP21,
    }

    def __init__( self, pin: int ):
        self.io = digitalio.DigitalInOut( self.BUTTON_PIN[pin] )
        self.io.direction = digitalio.Direction.INPUT
        self.io.pull      = digitalio.Pull.UP

    def pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise"
        return not self.io.value


class smallmotor:  # TODO
    "An object representing a servo"

    SERVO_PIN = {
        3: board.GP12,
        4: board.GP13,
        5: board.GP14,
        6: board.GP15,
    }

    def __init__( self, pin: int, direction: int = 1 ):
        self.io = servo.ContinuousServo( pwmio.PWMOut(
            self.SERVO_PIN[pin],
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


def pause( seconds: float = 0.05 ) -> None:
    "Wait the given number of seconds before moving on"
    time.sleep( seconds )

def until( condition ) -> None:
    "Wait until the given condition is satisfied"
    while not condition():
        pause()

# TODO: chopping block
def loop( code, condition = lambda : False ) -> None:
    """
    Loops the given code indefinitely or until the given termination condition
    is met
    """
    while not condition():
        code()
        pause()
