import math
from general.functions import wait
from motion.smallmotor import smallmotor
from motion.largemotor import largemotor

def calc_mods( direction: int, drift: float ) -> tuple[float, float]:
    """
    Calculates the constants that will be applied to the drivetrain's left
    and right motors to modify their power levels, so that they can drive
    straight despite drift.
    """
    if drift < 1:
        return (drift * direction, direction)
    else:
        return (direction, ( 1 / drift * direction ))

class drivetrain:
    "A drivetrain made from 2 large or small motors."

    def __init__(
        self,
        left_motor:  smallmotor | largemotor,
        right_motor: smallmotor | largemotor,
        direction:   int   = 1,
        drift:       float = 1
    ):
        self.__left_motor  = left_motor
        self.__right_motor = right_motor
        (self.__left_mod, self.__right_mod) = calc_mods(
            math.copysign( 1, direction ),
            drift
        )

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
        self.__left_motor.spin( left_speed * self.__left_mod )
        self.__right_motor.spin( right_speed * self.__right_mod )
        if seconds != None:
            wait( seconds )
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
        "Stops both motors."
        self.__left_motor.stop()
        self.__right_motor.stop()
