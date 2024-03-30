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

D_CYCLE = 2 ** 15  # duty cycle
FRQ     = 50       # frequency

button_pin = {
    20: board.GP20,
    21: board.GP21,
}
servo_pin = {
    12: board.GP12,
    13: board.GP13,
    14: board.GP14,
    15: board.GP15,
}
dc_pin = {
    8:  board.GP8,
    9:  board.GP9,
    10: board.GP10,
    11: board.GP11,
}

class button:
    "An object representing a button"

    def __init__( self, pin: int ):
        self.io = digitalio.DigitalInOut( button_pin[pin] )

    def is_pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise"
        return not self.io.value

class servo:
    "An object representing a servo"

    def __init__( self, pin: int ):
        pwm = pwmio.PWMOut(
            servo_pin[pin],
            duty_cycle = D_CYCLE,
            frequency  = FRQ
        )
        self.io = servo.Servo( pwm )

    def spin( self, speed: float ) -> None:
        "Spin the servo at the given speed"
        self.io.angle = speed
        # TODO: Stop the servo

class motor:
    "An object representing a DC motor"

    def __init__( self, pin1: int, pin2: int ):
        forward  = pwmio.PWMOut( dc_pin[pin1], frequency = FRQ )
        backward = pwmio.PWMOut( dc_pin[pin2], frequency = FRQ )
        self.io  = motor.DCMotor( forward, backward )

    def spin( self, speed: float, seconds: float = None ) -> None:
        """
        Spin the motor at the given speed for the given time period; if no
        period is given then it spins until stopped
        """
        self.io.throttle = speed
        if seconds != None:
            pause( seconds )
            self.io.spin( 0 )

def pause( seconds: float ) -> None:
    "Wait the given number of seconds before moving on"
    time.sleep( seconds )

def loop(
        code:      Callable[[], None],
        condition: Callable[[], bool] = lambda : False
    ) -> None:
    """
    Loops the given code indefinitely or until the given termination condition
    is met
    """
    while not condition():
        code()
        pause( 0.05 )
