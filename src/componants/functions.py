import time

def pause( seconds: float = 0.05 ) -> None:
    "Wait the given number of seconds before moving on"
    time.sleep( seconds )

def until( condition ) -> None:
    "Wait until the given condition is satisfied"
    while not condition():
        pause()

# TODO: chopping block
def loop( code, condition = lambda : False ) -> None:
    """
    Loops the given code indefinitely or until the given termination condition
    is met
    """
    while not condition():
        code()
        pause()
