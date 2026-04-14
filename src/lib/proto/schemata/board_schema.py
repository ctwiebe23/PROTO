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
        6: port(None, None, board.GP8, board.GP9),
        7: port(None, None, board.GP10, board.GP11),
        8: port(board.GP20),
        9: port(board.GP21),
        10: port(board.GP12),
        11: port(board.GP13),
        12: port(board.GP14),
        13: port(board.GP15),
        14: port(board.GP7, board.GP28),
        15: port(board.GP0, board.GP1),
    },
    start_button_port=8,
    builtin_light_port=1
)

PROTOBOARD_V1: board_schema = board_schema(
    ports={
        7:  port(board.GP26, board.GP11),
        6:  port(board.GP28, board.GP12),
        # 5:  port(board.GP29, board.GP13),  # requires custom uf2 file
        4:  port(board.GP27, board.GP10),
        3:  port(board.GP14, board.GP15, board.GP5, board.GP4),
        2:  port(board.GP16, board.GP17, board.GP3, board.GP2),
        1:  port(board.GP20, board.GP21, board.GP8, board.GP9),
        0:  port(board.GP18, board.GP19, board.GP6, board.GP7),
        8:  port(board.GP0),
        9:  port(board.GP1),
        10: port(board.GP23),
        11: port(board.GP22),
        12: port(board.GP25),
        13: port(board.GP24),
    },
    start_button_port=10,
    builtin_light_port=8,
)

PI_PICO: board_schema = board_schema(
    ports={
        25: port(board.GP25),
    }
)
