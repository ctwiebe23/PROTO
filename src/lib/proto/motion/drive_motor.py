import pwmio
from adafruit_motor import motor
import proto.system as system
from proto.schemata.motor_driver_schema import motor_driver_schema
from proto.general.functions import wait, sig_int


class drive_motor:
    "A DC motor plugged in to a drive port."

    def __init__(
        self, port: int, direction: int = 1, schema: motor_driver_schema = system.driver
    ):
        self.__schema = schema
        forward = pwmio.PWMOut(
            system.board[port].pin1, frequency=self.__schema.frequency
        )
        backward = pwmio.PWMOut(
            system.board[port].pin2, frequency=self.__schema.frequency
        )
        self.__io = motor.DCMotor(forward, backward)
        self.__direction = sig_int(direction)

    def spin(self, power: float, seconds: float = None) -> None:
        """
        Spin the motor at the given power for the given time period; if
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
        Spin the motor backwards at the given power for the given time
        period; if no period is given then it spins until stopped.
        """
        self.spin(-power, seconds)

    def stop(self) -> None:
        "Stops the motor."
        self.spin(0)
