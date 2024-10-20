import board
import digitalio
import neopixel
import simpleio
import time
import pwmio
from adafruit_motor import servo, motor

# Initialize LEDs
# LEDs placement on Maker Pi RP2040
LED_PINS = [board.GP0,
            board.GP1,
            board.GP2,
            board.GP3,
            board.GP4,
            board.GP5,
            board.GP6,
            board.GP7,
            board.GP16,
            board.GP17,
            board.GP26,
            board.GP27,
            board.GP28]

LEDS = []
for pin in LED_PINS:
    # Set pins as digital output
    digout = digitalio.DigitalInOut(pin)
    digout.direction = digitalio.Direction.OUTPUT
    LEDS.append(digout)





# -------------------------------------------------
# ON START: Show running light and play melody
# -------------------------------------------------
for i in range(len(LEDS)):
    LEDS[i].value = True

    if i < len(MELODY_NOTE):
        # Play melody tones
        simpleio.tone(PIEZO_PIN, MELODY_NOTE[i], duration=MELODY_DURATION[i])
    else:
        # Light up the remainding LEDs
        time.sleep(0.15)

# Turn off LEDs one-by-one very quickly
for i in range(len(LEDS)):
    LEDS[i].value = False
    time.sleep(0.02)


color = 0
state = 0

