import board
import digitalio
from base import *

class button:
    "An object representing a button"

    BUTTON_PIN = {
        1: (board.GP20, None),
        2: (board.GP21, None),
    }
    
    BUTTON_PIN.update(GROVE_PIN)

    def __init__( self, pinset: int ):
        self.io = digitalio.DigitalInOut( self.BUTTON_PIN[pinset][0] )
        self.io.direction = digitalio.Direction.INPUT
        self.io.pull      = digitalio.Pull.UP

    def pressed( self ) -> bool:
        "Returns true if the button is pressed, false otherwise"
        return not self.io.value
