import time
import board

# contains constants, variables, and functions used by multiple componants

# public constant for reversing servos and dc motors
reversed = -1

# motor frequency
FRQ = 50

# general pins corresponding to GROVE ports
GROVE_PIN = {
    9:  (board.GP2,  board.GP3),
    10: (board.GP4,  board.GP5),
    11: (board.GP16, board.GP17),
    12: (board.GP6,  board.GP26),
    13: (board.GP26, board.GP27),
}

def pause( seconds: float = 0.05 ) -> None:
    """
    Wait the given number of seconds before moving on. If no time is given,
    waits for 0.05 seconds.
    """
    time.sleep( seconds )

def until( condition ) -> None:
    "Wait until the given condition is satisfied."
    while not condition():
        pause()
