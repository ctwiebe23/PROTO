import board
import digitalio
from proto.general.constants    import GROVE_PORTS

BUTTON_PORTS = {
    8: (board.GP20, None),
    9: (board.GP21, None),
}

BUTTON_PORTS.update( GROVE_PORTS )

class button:
    "A button, either built into the board or plugged into a GROVE port."

    def __init__( self, port: int ):
        self.__io           = digitalio.DigitalInOut( BUTTON_PORTS[port][0] )
        self.__io.direction = digitalio.Direction.INPUT
        self.__io.pull      = digitalio.Pull.UP

    def __enter__( self ):
        return self

    def __exit__( self, exc_type, exc_value, exc_tb ):
        self.free_port()

    def pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise."
        return not self.__io.value

    def free_port( self ) -> None:
        "Frees the port for use by other buttons, disabling this one."
        self.__io.deinit()
