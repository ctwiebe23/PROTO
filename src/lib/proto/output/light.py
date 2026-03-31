import digitalio
import proto.system as system
from proto.general.functions import wait

class light:
    "A single LED."

    def __init__(self, port: int):
        self.__pin = system.board[port].pin1
        self.__io = digitalio.DigitalInOut(self.__pin)
        self.__io.direction = digitalio.Direction.OUTPUT
        self.__io.value = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.free_port()

    def on(self, seconds: float = None):
        "Turns the LED on."
        self.__io.value = True

        if seconds != None:
            wait(seconds)
            self.off()

    def off(self, seconds: float = None):
        "Turns the LED off."
        self.__io.value = False

        if seconds != None:
            wait(seconds)
            self.on()

    def toggle(self):
        "Toggles the LED on or off, whichever it currently isn't."
        if self.__io.value:
            self.__io.value = False
        else:
            self.__io.value = True

    def free_port(self) -> None:
        "Frees the port for use by other LEDs, disabling this one."
        self.__io.deinit()
