import board
import digitalio
import pwmio
import time
from adafruit_motor import servo

right  = digitalio.DigitalInOut(board.GP20)
right  = digitalio.Direction.INPUT
right  = digitalio.Pull.UP

motorA = servo.ContinuousServo(
  pwmio.PWMOut(board.GP12, frequency = 50)
)
motorE = servo.ContinuousServo(
  pwmio.PWMOut(board.GP13, frequency = 50)
)

speed  = 0.5

def Forward():
  motorA.throttle = speed
  motorE.throttle = speed
  time.sleep(2)
  motorA.throttle = 0
  motorE.throttle = 0

while True:
  if not right.value:
    Forward()
