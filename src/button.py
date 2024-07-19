import board
import digitalio

__BUTTON_PIN = {
    1: (board.GP20, None),
    2: (board.GP21, None),
}

__BUTTON_PIN.update(__GROVE_PIN)

class button:
    "An object representing a button"

    def __init__( self, pinset: int ):
        self.__io = digitalio.DigitalInOut( __BUTTON_PIN[pinset][0] )
        self.__io.direction = digitalio.Direction.INPUT
        self.__io.pull      = digitalio.Pull.UP

    def pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise"
        return not self.__io.value
