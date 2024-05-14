import board
import digitalio
import pwmio
import time
from adafruit_motor import servo

right  = digitalio.DigitalInOut(board.GP20)
right  = digitalio.Direction.INPUT
right  = digitalio.Pull.UP

moterA = servo.ContinuousServo(
  pwmio.PWMOut(board.GP12, frequency = 50)
)
moterB = servo.ContinuousServo(
  pwmio.PWMOut(board.GP13, frequency = 50)
)

speed  = 0.5

def Forward():
  moterA.throttle = speed
  moterB.throttle = speed * -1
  time.sleep(2)
  moterA.throttle = 0
  moterB.throttle = 0

while True:
  if not right.value:
    Forward()
