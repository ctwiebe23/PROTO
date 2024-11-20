import pwmio
from adafruit_motor             import servo
from proto.general.constants    import SYSTEM
from proto.general.functions    import wait, sig_int

class smallmotor:
    "A small motor plugged into a small motor port or GROVE port."

    def __init__( self, port: int, direction: int = 1 ):
        self.__io = servo.ContinuousServo(
            pwmio.PWMOut(
                SYSTEM.BOARD.PINSETS[port][0],
                frequency = SYSTEM.CSERVO.FREQUENCY,
            )
        )
        self.__direction = sig_int( direction )

    def spin( self, power: float, seconds: float = None ) -> None:
        """
        Spin the small motor at the given power for the given time period; if
        no period is given then it spins until stopped.
        """
        self.__io.throttle  = self.__direction \
                            * SYSTEM.CSERVO.POWER_SCALER( power )

        if seconds != None:
            wait( seconds )
            self.stop()

    def stop( self ) -> None:
        "Stops the small motor."
        self.spin( 0 )
