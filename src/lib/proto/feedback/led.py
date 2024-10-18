import board
import digitalio
from proto.general.functions import wait

LEDS = map( digitalio.DigitalInOut, [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP16,
    board.GP17,
    board.GP26,
    board.GP27,
    board.GP28,
] )

def led_on( led_port: int ) -> None:
    """
    Turns the given LED on.
    
    LED ports: 1 - 13
    """
    LEDS[led_port - 1].value = True
    
def led_off( led_port: int ) -> None:
    """
    Turns the given LED off.
    
    LED ports: 1 - 13
    """
    LEDS[led_port - 1].value = False

def led_blink( led_port: int, seconds: float = 0.15 ) -> None:
    """
    Lights up the LED at the given port for 0.15 seconds, unless a different
    amount of seconds is specified.
    
    LED ports: 1 - 13
    """
    led_on( led_port )
    wait( seconds )
    led_off( led_port )
