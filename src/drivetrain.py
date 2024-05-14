from functions import *
from smallmotor import *
from largemotor import *

class drivetrain:
    "A drivetrain consisting of 2 motors (small or large)"

    def __init__(
        self,
        lDrive: smallmotor | largemotor,
        rDrive: smallmotor | largemotor
    ):
        self.__lDrive = lDrive
        self.__rDrive = rDrive

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
        self.__lDrive.spin( lSpeed )
        self.__rDrive.spin( rSpeed )
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
        self.curve( speed, speed * -1, seconds )

    def stop( self ) -> None:
        self.__lDrive.stop()
        self.__rDrive.stop()
