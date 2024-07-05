# FYI: this code was auto-generated by BAPCAT as a pseudo-library from
#  its individual parts and should not be treated as the source code.
# Built on: 2024-07-05T12:18-05:00
from adafruit_motor import motor
from adafruit_motor import servo
import board
import digitalio
import math
import pwmio
import time
__FRQ = 50
__GROVE_PIN = {
    9:  (board.GP2,  board.GP3),
    10: (board.GP4,  board.GP5),
    11: (board.GP16, board.GP17),
    12: (board.GP6,  board.GP26),
    13: (board.GP26, board.GP27),
}
__largemotors = []
__smallmotors = []
reversed = -1
__BUTTON_PIN = {
    1: (board.GP20, None),
    2: (board.GP21, None),
}
__BUTTON_PIN.update(__GROVE_PIN)
class button:
    "An object representing a button"
    def __init__( self, pinset: int ):
        self.__io = digitalio.DigitalInOut( __BUTTON_PIN[pinset][0] )
        self.__io.direction = digitalio.Direction.INPUT
        self.__io.pull      = digitalio.Pull.UP
    def pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise"
        return not self.__io.value
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
        self.__direction = math.copysign( 1, direction )
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
class drivetrain:
    "A drivetrain consisting of 2 motors (small or large)"
    def __init__(
        self,
        lDrive:    smallmotor | largemotor,
        rDrive:    smallmotor | largemotor,
        direction: int   = 1,
        drift:     float = 1,
    ):
        self.__lDrive = lDrive
        self.__rDrive = rDrive
        (self.__lMod, self.__rMod) = self.__calcMods(
            math.copysign( 1, direction ),
            drift
        )
    def __calcMods( direction: int, drift: float ) -> tuple[float, float]:
        """
        Calculates the constants that will be applied to the drivetrain's left
        and right motors
        """
        if drift < 1:
          return (drift * direction, direction)
        else:
          return (direction, ( 1 / drift * direction ) )
    def curve(
        self,
        lSpeed:  float,
        rSpeed:  float,
        seconds: float = None
    ) -> None:
        """
        Spins both motors at different speeds. If a time is given, stops after
        the time has elapsed.
        """
        self.__lDrive.spin( lSpeed * self.__lMod )
        self.__rDrive.spin( rSpeed * self.__rMod )
        if seconds != None:
            pause( seconds )
            self.stop()
    def drive( self, speed: float, seconds: float = None ) -> None:
        """
        Spins both motors at the same speed. If a time is given, stops after
        the time has elapsed.
        """
        self.curve( speed, speed, seconds )
    def turn( self, speed: float, seconds: float = None ) -> None:
        """
        Rotates on the spot at the given speed. If a time is given, stops
        after that time has elapsed.
        """
        self.curve( speed, -speed, seconds )
    def stop( self ) -> None:
        self.__lDrive.stop()
        self.__rDrive.stop()
