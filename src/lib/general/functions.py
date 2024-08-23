import time

def wait( seconds: float = 0.05 ) -> None:
    """
    Wait the given number of seconds before moving on. If no time is given,
    waits for 0.05 seconds.
    """
    time.sleep( seconds )

def wait_until( condition ) -> None:
    "Wait until the given condition is satisfied."
    while not condition():
        wait()
