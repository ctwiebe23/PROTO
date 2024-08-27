import board

# public constant for reversing servos and dc motors
reversed = -1

# motor frequency
FRQ = 50

# general pins corresponding to GROVE ports
GROVE_PORTS = {
    9:  (board.GP2,     board.GP3),
    10: (board.GP4,     board.GP5),
    11: (board.GP16,    board.GP17),
    12: (board.GP6,     board.GP26),
    13: (board.GP26,    board.GP27),
}
