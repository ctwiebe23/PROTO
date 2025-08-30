import pwmio
from adafruit_motor import servo
import proto.system as system
from proto.schemata.cservo_schema import cservo_schema
from proto.general.functions import wait, sig_int


class smallmotor:
    "A small motor plugged into a small motor port or GROVE port."

    def __init__(
        self,
        port: int,
        direction: int = 1,
        schema: cservo_schema = system.cservo,
    ):
        self.__schema = schema
        self.__io = servo.ContinuousServo(
            pwmio.PWMOut(
                system.board[port].pin1,
                frequency=self.__schema.frequency,
            )
        )
        self.__direction = sig_int(direction)

    def spin(self, power: float, seconds: float = None) -> None:
        """
        Spin the small motor at the given power for the given time period; if
        no period is given then it spins until stopped.
        """
        self.__io.throttle = self.__direction * self.__schema.power_scaler(
            power
        )

        if seconds != None:
            wait(seconds)
            self.stop()

    def spin_back(self, power: float, seconds: float = None) -> None:
        """
        Spin the small motor backwards at the given power for the given time
        period; if no period is given then it spins until stopped.
        """
        self.spin(-power, seconds)

    def stop(self) -> None:
        "Stops the small motor."
        self.spin(0)
