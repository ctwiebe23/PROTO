import pwmio
from adafruit_motor             import servo as adafruit_servo
from proto.general.system_specs import SYSTEM
from proto.general.functions    import clamp

class servo:
    "A servo motor plugged into a small motor port or GROVE port."
    
    def __init__( self, port: int ):
        self.__io = adafruit_servo.Servo(
            pwmio.PWMOut(
                SYSTEM.board.ports[port].pin1,
                duty_cycle=SYSTEM.servo.duty_cycle,
                frequency=SYSTEM.servo.frequency,
            )
        )

    def moveto( self, angle: float ) -> None:
        "Rotates the servo to the given angle."
        self.__io.angle = clamp( 0, angle, 180 )
