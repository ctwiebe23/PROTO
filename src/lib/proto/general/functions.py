from math import copysign
from time import sleep
from typing import Callable

def wait( seconds: float = 0.05 ) -> None:
    """
    Wait the given number of seconds before moving on. If no time is given,
    waits for 0.05 seconds.
    """
    sleep( seconds )

def wait_until( condition: Callable[[], bool] ) -> None:
    "Wait until the given condition is satisfied."
    while not condition():
        wait()

def sig_int( number: float ) -> int:
    "Returns the sign of the given number; either 1 or -1."
    return copysign( 1, number )

def clamp( min_bound: float, x: float, max_bound: float ) -> float:
    "Bounds the given number between the given minimium and maximium bounds."
    return max( min_bound, min( x, max_bound ) )

def generate_speed_bounder(
    interval: tuple[float, float]
) -> Callable[[float], float]:
    """
    Returns a function that bounds a speed between the interval [-100, 100]
    and then scales it to the given positive interval.
    """
    range = interval[1] - ( offset := interval[0] )
    ratio = range / 100
    
    def speed_bounder( speed: float ) -> float:
        "Converts the given speed to a valid value."
        if speed == 0:
            return 0
        
        speed = clamp( -100, speed, 100 )
        
        return ( abs( speed ) * ratio + offset ) * sig_int( speed )
    
    return speed_bounder
