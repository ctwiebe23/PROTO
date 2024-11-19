import board
import pwmio
from adafruit_motor             import motor
from proto.general.constants    import FRQ
from proto.general.functions    import wait, sig_int, bound_power

DC_PORTS = {
    6: (board.GP8,  board.GP9),
    7: (board.GP10, board.GP11),
}

DC_THROTTLE_RANGE = (0.3, 1)

class largemotor:
    "A large motor plugged in to a large motor port."

    def __init__( self, port: int, direction: int = 1 ):
        forward     = pwmio.PWMOut( DC_PORTS[port][0], frequency = FRQ )
        backward    = pwmio.PWMOut( DC_PORTS[port][1], frequency = FRQ )
        self.__io   = motor.DCMotor( forward, backward )
        self.__direction = sig_int( direction )

    def spin( self, power: float, seconds: float = None ) -> None:
        """
        Spin the large motor at the given power for the given time period; if
        no period is given then it spins until stopped.
        """
        self.__io.throttle = self.__direction * bound_power(
            power,
            DC_THROTTLE_RANGE,
        )

        if seconds != None:
            wait( seconds )
            self.stop()

    def stop( self ) -> None:
        "Stops the large motor."
        self.spin( 0 )
