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

CYCLE = 2 ** 15  # duty cycle
FRQ   = 50       # frequency

BUTTON_PIN = {
    1: board.GP20,
    2: board.GP21,
}
DC_PIN = {
    7: (board.GP8 , board.GP9 ),
    8: (board.GP10, board.GP11),
}
SERVO_PIN = {
    3: board.GP12,
    4: board.GP13,
    5: board.GP14,
    6: board.GP15,
}

class button:
    "An object representing a button"

    def __init__( self, pin: int ):
        self.io           = digitalio.DigitalInOut( BUTTON_PIN[pin] )
        self.io.direction = digitalio.Direction.INPUT
        self.io.pull      = digitalio.Pull.UP

    def pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise"
        return not self.io.value

class smallmotor:
    "An object representing a servo"

    def __init__( self, pin: int ):
        self.io = smallmotor.Servo( pwmio.PWMOut(
            SERVO_PIN[pin],
            duty_cycle = CYCLE,
            frequency  = FRQ
        ))

    def spin( self, speed: float ) -> None:
        "Spin the servo at the given speed"
        self.io.angle = speed
        # TODO: Stop the servo

class largemotor:
    "An object representing a DC motor"

    def __init__( self, pinset: int ):
        forward  = pwmio.PWMOut( DC_PIN[pinset][0], frequency = FRQ )
        backward = pwmio.PWMOut( DC_PIN[pinset][1], frequency = FRQ )
        self.io  = motor.DCMotor( forward, backward )

    def spin( self, speed: float, seconds: float = None ) -> None:
        """
        Spin the motor at the given speed for the given time period; if no
        period is given then it spins until stopped
        """
        speed = 100 if speed > 100 else -100 if speed < -100 else speed
        self.io.throttle = speed / 100
        if seconds != None:
            pause( seconds )
            self.io.spin( 0 )

def pause( seconds: float = 0.05 ) -> None:
    "Wait the given number of seconds before moving on"
    time.sleep( seconds )

def until( condition ) -> None:
    "Wait until the given condition is satisfied"
    while not condition():
        pause()

def loop( code, condition = lambda : False ) -> None:
    """
    Loops the given code indefinitely or until the given termination condition
    is met
    """
    while not condition():
        code()
        pause()
