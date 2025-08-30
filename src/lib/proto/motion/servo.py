import pwmio
from adafruit_motor import servo as adafruit_servo
import proto.system as system
from proto.schemata.servo_schema import servo_schema
from proto.general.functions import clamp, wait


class servo:
    "A servo motor plugged into a small motor port or GROVE port."

    def __init__(self, port: int, schema: servo_schema = system.servo):
        self.__schema = schema
        self.__io = adafruit_servo.Servo(
            pwmio.PWMOut(
                system.board[port].pin1,
                duty_cycle=self.__schema.duty_cycle,
                frequency=self.__schema.frequency,
            )
        )

    def moveto(self, angle: float, seconds: float = None) -> None:
        "Rotates the servo to the given angle."
        self.__io.angle = clamp(0, angle, 180)

        if seconds != None:
            wait(seconds)
