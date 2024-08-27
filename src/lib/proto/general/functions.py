from math import copysign
from time import sleep

def wait( seconds: float = 0.05 ) -> None:
    """
    Wait the given number of seconds before moving on. If no time is given,
    waits for 0.05 seconds.
    """
    sleep( seconds )

def wait_until( condition: function[[], bool] ) -> None:
    "Wait until the given condition is satisfied."
    while not condition():
        wait()

def sig_int( number: float | int ) -> int:
    "Returns the sign of the given number."
    return copysign( 1, number )

def speed_bounder( interval: tuple[float, float] ) -> function[[float], float]:
    """
    Returns a function that bounds a speed between the given interval.
    """
    range = interval[1] - ( offset := interval[0] )
    ratio = range / 100
    
    return lambda x : 0 if x == 0 \
                        else ( abs( x ) * ratio + offset ) * sig_int( x )
