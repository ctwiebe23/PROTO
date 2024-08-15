import board
import digitalio
from c0_core import GROVE_PORTS

__BUTTON_PORTS = {
    1: (board.GP20, None),
    2: (board.GP21, None),
}

__BUTTON_PORTS.update(GROVE_PORTS)

class button:
    "A button, either built into the board or plugged into a GROVE port."

    def __init__( self, port: int ):
        self.__io = digitalio.DigitalInOut( __BUTTON_PORTS[port][0] )
        self.__io.direction = digitalio.Direction.INPUT
        self.__io.pull      = digitalio.Pull.UP

    def pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise."
        return not self.__io.value
