import board
import digitalio
import time
import pwmio
from adafruit_motor import servo, motor

"""
Carston Wiebe
carstonwiebe17@gmail.com

CIRCUITPYTHON code to test the Maker PI RP2040 with servos and dc motors
"""

def create_button( pin ) -> digitialio:
    """
    Takes a `pin` in the style of `board.GP<pin #>` and returns a button
    made using `digitialio`
    """
    return digitalio.DigitalInOut( pin )


def create_servo( pin, d_cycle: int, frq: int ) -> servo:
    """
    Takes a `pin` in the style of `board.GP<pin #>`, a `duty_cycle` and a
    `frequency`; returns a servo motor made using `pwmio`
    """
    return servo.Servo( pwmio.PWMOut( pin, duty_cycle = d_cycle, frequency = frq ) )

def create_DC( pin1, pin2, frq: int ) -> motor:
    """
    Takes two `pin`s in the style of `board.GP<pin #>` and a `frequency`;
    returns a DC motor made using `pwmio`
    """
    forward  = pwmio.PWMOut( pin1, frequency = frq )
    backward = pwmio.PWMOut( pin2, frequency = frq )
    return motor.DCMotor( forward, backward )


def is_pressed( button: digitalio ) -> bool:
    "Returns true if `button` is pressed, false otherwise"
    return not button.value

D_CYCLE = 2 ** 15  # TODO
FRQ     = 50       # TODO

servo_pins = [
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
]

button1 = create_button( board.GP20 )
button2 = create_button( board.GP21 )

# servos = [ create_servo( p, D_CYCLE, FRQ ) for p in servo_pins ]
servo = create_servo( board.GP15, D_CYCLE, FRQ )

DC_1 = create_DC( board.GP8,  board.GP9,  FRQ )
DC_2 = create_DC( board.GP10, board.GP11, FRQ )

while True:

    if is_pressed( button1 ):
        # for servo in servos:
        #     servo.angle = 0
        servo.angle = 0

        DC_1.throttle =  0.5
        DC_2.throttle = -0.5

    if is_pressed( button2 ):
        # for servo in servos:
        #     servo.angle = 180
        servo.angle = 180

        DC_1.throttle = 0
        DC_2.throttle = 0

    time.sleep( 0.05 )
