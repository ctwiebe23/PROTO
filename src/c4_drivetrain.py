import math
from c0_core import pause
from c2_small_motor import small_motor
from c3_large_motor import large_motor

class drivetrain:
    "A drivetrain made from 2 large or small motors."

    def __init__(
        self,
        left_motor:  small_motor | large_motor,
        right_motor: small_motor | large_motor,
        direction:   int   = 1,
        drift:       float = 1,
    ):
        self.__left_motor  = left_motor
        self.__right_motor = right_motor
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
        time:        float = None
    ) -> None:
        """
        Spins both motors at different speeds. If a time is given, stops after
        the time has elapsed.
        """
        self.__left_motor.spin( left_speed * self.__left_mod )
        self.__right_motor.spin( right_speed * self.__right_mod )
        if time != None:
            pause( time )
            self.stop()

    def drive( self, speed: float, time: float = None ) -> None:
        """
        Spins both motors at the same speed. If a time is given, stops after
        the time has elapsed.
        """
        self.curve( speed, speed, time )

    def turn( self, speed: float, time: float = None ) -> None:
        """
        Rotates on the spot at the given speed. If a time is given, stops
        after that time has elapsed.
        """
        self.curve( speed, -speed, time )

    def stop( self ) -> None:
        "Stops both motors."
        self.__left_motor.stop()
        self.__right_motor.stop()
