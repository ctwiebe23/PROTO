import board
import digitalio
from alpha import *

__BUTTON_PIN = {
    1: (board.GP20, None),
    2: (board.GP21, None),
}

__BUTTON_PIN.update(GROVE_PIN)

class button:
    "A button, either built into the board or plugged into a GROVE port."

    def __init__( self, pinset: int ):
        self.__io = digitalio.DigitalInOut( __BUTTON_PIN[pinset][0] )
        self.__io.direction = digitalio.Direction.INPUT
        self.__io.pull      = digitalio.Pull.UP

    def pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise."
        return not self.__io.value
