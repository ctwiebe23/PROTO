from functions import *
from smallmotor import *
from largemotor import *
import math

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
