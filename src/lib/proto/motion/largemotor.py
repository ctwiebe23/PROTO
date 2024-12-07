import pwmio
from adafruit_motor             import motor
from proto.general.system_specs import SYSTEM
from proto.general.functions    import wait, sig_int

class largemotor:
    "A large motor plugged in to a large motor port."

    def __init__( self, port: int, direction: int = 1 ):
        forward     = pwmio.PWMOut(
            SYSTEM.board.ports[port].pin1,
            frequency=SYSTEM.dc.frequency
        )
        backward    = pwmio.PWMOut(
            SYSTEM.board.ports[port].pin2,
            frequency=SYSTEM.dc.frequency
        )
        self.__io   = motor.DCMotor( forward, backward )
        self.__direction = sig_int( direction )

    def spin( self, power: float, seconds: float = None ) -> None:
        """
        Spin the large motor at the given power for the given time period; if
        no period is given then it spins until stopped.
        """
        self.__io.throttle = self.__direction * SYSTEM.dc.power_scaler( power )

        if seconds != None:
            wait( seconds )
            self.stop()

    def stop( self ) -> None:
        "Stops the large motor."
        self.spin( 0 )
