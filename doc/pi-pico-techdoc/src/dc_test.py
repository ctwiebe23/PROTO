from machine import PWM

"""
Component | Pin
Servo     | 0
"""


def clamp(lower_bound: float, x: float, upper_bound: float) -> float:
    return min(upper_bound, max(lower_bound, x))


class c_servo_schema:
    def __init__(self, freq_hz: int, range_ns: int, center_ns: int):
        self.freq_hz = freq_hz
        self.range_ns = range_ns
        self.center_ns = center_ns


class system_schema:
    def __init__(self, c_servo: c_servo_schema = None):
        self.c_servo = c_servo


SYSTEM = system_schema(
    c_servo=c_servo_schema(
        freq_hz=50,
        range_ns=2_300e3 - 700e3,
        center_ns=1_500e3,
    ),
)


class c_servo:
    def __init__(self, pin: int):
        self.pwm = PWM(
            pin, freq=SYSTEM.c_servo.freq_hz, duty_ns=SYSTEM.c_servo.center_ns
        )

    def forwards(self, speed: float) -> None:
        speed = clamp(-100, speed, 100) / 100  # range of [-1,1]
        speed *= SYSTEM.c_servo.range_ns / 2  # range of the servo
        speed += SYSTEM.c_servo.center_ns  # center the range
        self.pwm.duty_ns(speed)

    def backwards(self, speed: float) -> None:
        self.forwards(-speed)

    def stop(self) -> None:
        self.forwards(0)


cs = c_servo(0)
cs.forwards(100)
