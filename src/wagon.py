from functions import *
from small_motor import *
from large_motor import *
import math

class wagon:
    "A drivetrain made from 2 large or small motors."

    def __init__(
        self,
        lDrive:    small_motor | large_motor,
        rDrive:    small_motor | large_motor,
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
        and right motors to modify their power levels, so that they can drive
        straight despite drift.
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
