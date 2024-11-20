import board
import pwmio
from adafruit_motor             import motor
from proto.general.constants    import SYSTEM
from proto.general.functions    import wait, sig_int, bound_power

class largemotor:
    "A large motor plugged in to a large motor port."

    def __init__( self, port: int, direction: int = 1 ):
        forward     = pwmio.PWMOut(
            SYSTEM.BOARD.PINSETS[port][0],
            frequency = SYSTEM.DC.FREQUENCY
        )
        backward    = pwmio.PWMOut(
            SYSTEM.BOARD.PINSETS[port][1],
            frequency = SYSTEM.DC.FREQUENCY
        )
        self.__io   = motor.DCMotor( forward, backward )
        self.__direction = sig_int( direction )

    def spin( self, power: float, seconds: float = None ) -> None:
        """
        Spin the large motor at the given power for the given time period; if
        no period is given then it spins until stopped.
        """
        self.__io.throttle = self.__direction * SYSTEM.DC.POWER_SCALER( power )

        if seconds != None:
            wait( seconds )
            self.stop()

    def stop( self ) -> None:
        "Stops the large motor."
        self.spin( 0 )
