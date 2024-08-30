from math import copysign
from time import sleep

def wait( seconds: float = 0.05 ) -> None:
    """
    Wait the given number of seconds before moving on. If no time is given,
    waits for 0.05 seconds.
    """
    sleep( seconds )

def wait_until( condition ) -> None:
    "Wait until the given condition (type: () -> bool) is satisfied."
    while not condition():
        wait()

def sig_int( number: float ) -> int:
    "Returns the sign of the given number; either 1 or -1."
    return copysign( 1, number )

def clamp( min_bound: float, x: float, max_bound: float ) -> float:
    "Bounds the given number between the given minimium and maximium bounds."
    return max( min_bound, min( x, max_bound ) )

def bound_speed( speed: float, interval: tuple[float, float] ) -> float:
    "Bounds the given speed between the given interval."
    if speed == 0:
        return 0
    
    speed = clamp( -100, speed, 100 )
    range = interval[1] - ( offset := interval[0] )
    ratio = range / 100
    
    return ( speed * ratio ) + ( offset * sig_int( speed ) )
