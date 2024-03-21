import time
import make

button_1 = create_button( board.GP20 )
button_2 = create_button( board.GP21 )

frequency = 50
DC_1 = create_DC( board.GP8,  board.GP9,  frequency )
DC_2 = create_DC( board.GP10, board.GP11, frequency )

while True:

    if is_pressed( button_1 ):

        DC_1.throttle =  0.5
        DC_2.throttle = -0.5

    if is_pressed( button_2 ):

        DC_1.throttle = 0
        DC_2.throttle = 0

    time.sleep( 0.05 )
