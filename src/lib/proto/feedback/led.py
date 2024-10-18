import board
import digitalio
from proto.general.functions import wait

LEDS = map( digitalio.DigitalInOut, [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP16,
    board.GP17,
    board.GP26,
    board.GP27,
    board.GP28,
] )

class led:
    "An LED built into the board on LED ports 1-13"

    def __init__( self, led_port: int ):
        self.__io = LEDS[led_port - 1]
        
    def off( self ) -> None:
        "Turns the LED off."
        self.__io.value = False
    
    def on( self, seconds: float = None ) -> None:
        """
        Turns the LED on, and if a number of seconds are given shuts it off
        after that many seconds.
        """
        self.__io.value = True
        if seconds != None:
            wait( seconds )
            self.off()
