import board

# public constant for reversing servos and dc motors
reversed = -1

# motor frequency
FRQ = 50

# general pins corresponding to GROVE ports
GROVE_PORTS = {
    1: (board.GP2,  board.GP3),
    2: (board.GP4,  board.GP5),
    3: (board.GP16, board.GP17),
    4: (board.GP6,  board.GP26),
    5: (board.GP26, board.GP27),
}
