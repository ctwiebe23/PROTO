import board
import digitalio
import time
import pwmio
from adafruit_motor import servo, motor
from typing import Callable

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
SERVO_PIN = {
    1: board.GP12,
    2: board.GP13,
    3: board.GP14,
    4: board.GP15,
}
DC_PIN = {
    1: (board.GP8,  board.GP9 ),
    2: (board.GP10, board.GP11),
}

class button:
    "An object representing a button"

    def __init__( self, pin: int ):
        self.io = digitalio.DigitalInOut( BUTTON_PIN[pin] )

    def is_pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise"
        return not self.io.value

class servo:
    "An object representing a servo"

    def __init__( self, pin: int ):
        pwm = pwmio.PWMOut( SERVO_PIN[pin], duty_cycle = CYCLE, frequency = FRQ )
        self.io = servo.Servo( pwm )

    def spin( self, speed: float ) -> None:
        "Spin the servo at the given speed"
        self.io.angle = speed
        # TODO: Stop the servo

class motor:
    "An object representing a DC motor"

    def __init__( self, pinset: int ):
        forward    = pwmio.PWMOut( DC_PIN[pinset][0], frequency = FRQ )
        backward   = pwmio.PWMOut( DC_PIN[pinset][1], frequency = FRQ )
        self.io    = motor.DCMotor( forward, backward )

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

def pause( seconds: float ) -> None:
    "Wait the given number of seconds before moving on"
    time.sleep( seconds )

def pause_until( condition: Callable[[], bool] ) -> None:
    "Wait until the given condition is satisfied"
    while not condition():
        pause( 0.05 )

def loop( code: Callable[[], None], condition: Callable[[], bool] = lambda : False ) -> None:
    """
    Loops the given code indefinitely or until the given termination condition
    is met
    """
    while not condition():
        code()
        pause( 0.05 )
