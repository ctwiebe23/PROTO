import digitalio
from proto.general.constants    import SYSTEM
from proto.general.functions    import wait_until

class button:
    "A button, either built into the board or plugged into a GROVE port."

    def __init__( self, port: int ):
        self.__pin  = SYSTEM.BOARD.PINSETS[port][0]
        self.__io   = digitalio.DigitalInOut( self.__pin )
        self.__io.direction = digitalio.Direction.INPUT
        self.__io.pull      = digitalio.Pull.UP
        self.__curr_value   = False

    def __enter__( self ):
        return self

    def __exit__( self, exc_type, exc_value, exc_tb ):
        self.free_port()

    def pressed( self, debounce: bool = True ) -> bool:
        "Returns true if the button is pressed, false otherwise."
        prev_value          = self.__curr_value  # for debouncing
        self.__curr_value   = not self.__io.value
        
        return self.__curr_value and (not prev_value or not debounce)
    
    def wait_until_pressed( self ) -> None:
        "Waits until the button is pressed."
        wait_until( self.pressed )
        
    def wait_while_pressed( self ) -> None:
        "Waits while the button is pressed."
        wait_until( lambda : not self.pressed( debounce=False ) )

    def free_port( self ) -> None:
        "Frees the port for use by other buttons, disabling this one."
        self.__io.deinit()
