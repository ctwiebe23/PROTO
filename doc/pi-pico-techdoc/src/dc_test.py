import utime
from machine import Pin, PWM

DCGM_N50_FREQ = 50


def setup() -> None:
    pos = PWM(0, freq=DCGM_N50_FREQ)
    neg = PWM(1, freq=DCGM_N50_FREQ)

    pos.duty_u16(0xFFFF)
    neg.duty_u16(0)


def loop() -> None:
    utime.sleep(1)


setup()
while True:
    loop()
