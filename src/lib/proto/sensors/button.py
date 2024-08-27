import board
import digitalio
from proto.general.constants import GROVE_PORTS

BUTTON_PORTS = {
    1: (board.GP20, None),
    2: (board.GP21, None),
}

BUTTON_PORTS.update( GROVE_PORTS )

class button:
    "A button, either built into the board or plugged into a GROVE port."

    def __init__( self, port: int ):
        self.__io = digitalio.DigitalInOut( BUTTON_PORTS[port][0] )
        self.__io.direction = digitalio.Direction.INPUT
        self.__io.pull      = digitalio.Pull.UP

    def pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise."
        return not self.__io.value
