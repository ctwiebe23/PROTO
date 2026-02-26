import board


class port:
    "Represents a port on a board with at least one pin."

    def __init__(self, pin1: any, pin2: any = None, dc1: any = None, dc2: any = None):
        self.pin1 = pin1
        self.pin2 = pin2
        self.dc1 = dc1
        self.dc2 = dc2


class board_schema:
    """
    A board schema that details available ports.  A port is a pair of pins
    or single pin that corresponds to a
    numbered port -- thus, the `ports` argument should be a dict of ports.

    The ports should be set up so the defined pin is the 'primary' pin that
    will always be used, while the second pin is only for components (such as
    DCs) that require two pins be grouped in the same 'port' -- for buttons and
    servos, only the first pin in the set will be used.
    
    The start button is the button that needs to be pressed for the user's
    program to start running.  Its value should be the index of the button's
    port on the board.
    
    The built-in light is an LED on the board that turns on once the user's
    program is ready to start, and turns off once it has started.  Its value
    should be the index of the LED's port on the board.
    """

    def __init__(self, ports: dict[int, port], start_button_port: int = None, builtin_light_port: int = None):
        self.ports = ports
        self.start_button_port = start_button_port
        self.builtin_light_port = builtin_light_port

    def __getitem__(self, index):
        return self.ports[index]


# =============================================================================#
# PRESETS
# =============================================================================#

MAKERPI_RP2040: board_schema = board_schema(
    ports={
        1: port(board.GP2, board.GP3),
        2: port(board.GP4, board.GP5),
        3: port(board.GP16, board.GP17),
        4: port(board.GP6, board.GP26),
        5: port(board.GP26, board.GP27),
        6: port(board.GP8, board.GP9),    # convert to new DC scheme
        7: port(board.GP10, board.GP11),  # convert to new DC scheme
        8: port(board.GP20, None),
        9: port(board.GP21, None),
        10: port(board.GP12, None),
        11: port(board.GP13, None),
        12: port(board.GP14, None),
        13: port(board.GP15, None),
        14: port(board.GP7, board.GP28),
        15: port(board.GP0, board.GP1),
    },
    start_button_port=8,
    builtin_light_port=1
)

PI_PICO: board_schema = board_schema(
    ports={
        1: port(board.GP0, None),
        2: port(board.GP1, None),
    },
)

PROTOBOARD_V1: board_schema = board_schema(
    ports={
        0: port(board.GP0),
        1: port(board.GP1),
        # 25: port(board.GP25),
    },
    start_button_port=25,
    builtin_light_port=0,
)
