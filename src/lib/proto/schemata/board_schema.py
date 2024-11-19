import board

class board_schema:
    """
    A control center schema that details availble ports.  A port list is a
    dictionary that maps an integer (the visible port number) to a tuple that
    models a pair of on-board pins.

    The schema will include the 4-pin ports in the 3-pin port list
    automatically (likewise, it includes both in the 1-pin port list).  To
    disable this behavor, set `concat_ports` to false.

    1-pin ports:
        1 pin is signal.
        The tuple should look like `(<signal pin>,None)`.

    3-pin ports:
        1 pin is GND, 1 power, and 1 signal.
        The tuple should look like `(<signal pin>,None)`.

    4-pin ports:
        1 pin is GND, 1 power, and 2 signals.
        The tuple should look like `(<signal pin 1>,<signal pin 2>)`.

    DC ports:
        1 pin is left, 1 right.
        The tuple should look like `(<left pin>,<right pin>)`.
    """

    def __init__(
        self,
        one_pin_ports:      dict[int,tuple[any,any]]    = None,
        three_pin_ports:    dict[int,tuple[any,any]]    = None,
        four_pin_ports:     dict[int,tuple[any,any]]    = None,
        dc_ports:           dict[int,tuple[any,any]]    = None,
        concat_ports:       bool                        = True,
    ):
        self.ONE_PIN_PORTS      = one_pin_ports
        self.THREE_PIN_PORTS    = three_pin_ports
        self.FOUR_PIN_PORTS     = four_pin_ports
        self.DC_PORTS           = dc_ports
        
        if concat_ports:
            if self.THREE_PIN_PORTS != None and self.FOUR_PIN_PORTS != None:
                self.THREE_PIN_PORTS.update( self.FOUR_PIN_PORTS )
            if self.ONE_PIN_PORTS != None and self.THREE_PIN_PORTS != None:
                self.ONE_PIN_PORTS.update( self.THREE_PIN_PORTS )

#=============================================================================#
# PRESETS
#=============================================================================#

MAKERPI_RP2040: board_schema = board_schema(
    one_pin_ports={
        8:  (board.GP20,None),
        9:  (board.GP21,None),
    },
    three_pin_ports={
        10: (board.GP12,None),
        11: (board.GP13,None),
        12: (board.GP14,None),
        13: (board.GP15,None),
    },
    four_pin_ports={
        1:  (board.GP2, board.GP3),
        2:  (board.GP4, board.GP5),
        3:  (board.GP16,board.GP17),
        4:  (board.GP6, board.GP26),
        5:  (board.GP26,board.GP27),
    },
    dc_ports={
        6:  (board.GP8, board.GP9),
        7:  (board.GP10,board.GP11),
    }
)
