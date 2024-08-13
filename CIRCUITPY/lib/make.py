# FYI: this code was auto-generated by BAPCAT as a pseudo-library from
#      its individual parts and should not be treated as the source
#      code.
# Built on: 2024-08-13T14:47:59-05:00
from adafruit_motor import motor
from adafruit_motor import servo
import board
import digitalio
import math
import pwmio
import time
# Built on: 2024-08-13T14:47:59-05:00
reversed = -1
FRQ = 50
GROVE_PIN = {
    9:  (board.GP2,  board.GP3),
    10: (board.GP4,  board.GP5),
    11: (board.GP16, board.GP17),
    12: (board.GP6,  board.GP26),
    13: (board.GP26, board.GP27),
}
def pause( seconds: float = 0.05 ) -> None:
    """
    Wait the given number of seconds before moving on. If no time is given,
    waits for 0.05 seconds.
    """
    time.sleep( seconds )
def until( condition ) -> None:
    "Wait until the given condition is satisfied."
    while not condition():
        pause()
__BUTTON_PIN = {
    1: (board.GP20, None),
    2: (board.GP21, None),
}
__BUTTON_PIN.update(GROVE_PIN)
class button:
    "A button, either built into the board or plugged into a GROVE port."
    def __init__( self, pinset: int ):
        self.__io = digitalio.DigitalInOut( __BUTTON_PIN[pinset][0] )
        self.__io.direction = digitalio.Direction.INPUT
        self.__io.pull      = digitalio.Pull.UP
    def pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise."
        return not self.__io.value
__SERVO_PIN = {
    3: (board.GP12, None),
    4: (board.GP13, None),
    5: (board.GP14, None),
    6: (board.GP15, None),
}
__SERVO_PIN.update(GROVE_PIN)
class small_motor:
    "A small motor plugged into a small motor port or GROVE port."
    def __init__( self, pinset: int, direction: int = 1 ):
        self.__io = servo.ContinuousServo( pwmio.PWMOut(
            __SERVO_PIN[pinset][0],
            frequency = FRQ
        ))
        self.__direction = math.copysign( 1, direction )
    def spin( self, speed: float, seconds: float = None ) -> None:
        """
        Spin the small motor at the given speed for the given time period; if
        no period is given then it spins until stopped.
        """
        speed = 100 if speed > 100 else -100 if speed < -100 else speed
        self.__io.throttle = speed / 100 * self.__direction
        if seconds != None:
            pause( seconds )
            self.stop()
    def stop( self ) -> None:
        "Stops the small motor."
        self.spin( 0 )
__DC_PIN = {
    7: (board.GP8,  board.GP9),
    8: (board.GP10, board.GP11),
}
class large_motor:
    "A large motor plugged in to a large motor port."
    def __init__( self, pinset: int, direction: int = 1 ):
        forward   = pwmio.PWMOut( __DC_PIN[pinset][0], frequency = FRQ )
        backward  = pwmio.PWMOut( __DC_PIN[pinset][1], frequency = FRQ )
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
            pause( seconds )
            self.stop()
    def stop( self ) -> None:
        "Stops the large motor."
        self.spin( 0 )
class drivetrain:
    "A drivetrain made from 2 large or small motors."
    def __init__(
        self,
        left_drive:  small_motor | large_motor,
        right_drive: small_motor | large_motor,
        direction:   int   = 1,
        drift:       float = 1,
    ):
        self.__left_drive  = left_drive
        self.__right_drive = right_drive
        (self.__left_mod, self.__right_mod) = self.__calc_mods(
            math.copysign( 1, direction ),
            drift
        )
    def __calc_mods( direction: int, drift: float ) -> tuple[float, float]:
        """
        Calculates the constants that will be applied to the drivetrain's left
        and right motors to modify their power levels, so that they can drive
        straight despite drift.
        """
        if drift < 1:
          return (drift * direction, direction)
        else:
          return (direction, ( 1 / drift * direction ) )
    def curve(
        self,
        left_speed:  float,
        right_speed: float,
        seconds:     float = None
    ) -> None:
        """
        Spins both motors at different speeds. If a time is given, stops after
        the time has elapsed.
        """
        self.__left_drive.spin( left_speed * self.__left_mod )
        self.__right_drive.spin( right_speed * self.__right_mod )
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
        self.__left_drive.stop()
        self.__right_drive.stop()
until(button(1).pressed)
