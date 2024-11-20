import board

class board_schema:
    """
    A board schema that details available ports.  A pinset is a pair of pins
    or single pin (represented by a tuple of size 2) that corresponds to a
    numbered port -- thus, the `pinsets` argument should be a dict of tuples.
    
    The pinsets should be set up so the left-most element of the tuple is
    always defined, while the second element is only for components (such as
    DCs) that require two pins be grouped in the same 'port' -- for buttons
    and servos, only the first pin in the set will be used.
    """

    def __init__( self, pinsets: dict[int, tuple[any,any]] ):
        self.PINSETS = pinsets

#=============================================================================#
# PRESETS
#=============================================================================#

MAKERPI_RP2040: board_schema = board_schema(
    pinsets={
        1:  (board.GP2, board.GP3),
        2:  (board.GP4, board.GP5),
        3:  (board.GP16,board.GP17),
        4:  (board.GP6, board.GP26),
        5:  (board.GP26,board.GP27),
        6:  (board.GP8, board.GP9),
        7:  (board.GP10,board.GP11),
        8:  (board.GP20,None),
        9:  (board.GP21,None),
        10: (board.GP12,None),
        11: (board.GP13,None),
        12: (board.GP14,None),
        13: (board.GP15,None),
        14: (board.GP7, board.GP28),
        15: (board.GP0, board.GP1),
    },
)
