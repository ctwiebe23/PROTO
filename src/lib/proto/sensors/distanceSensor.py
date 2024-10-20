import time
import board
import digitalio
import pulseio
import neopixel
import simpleio
import pwmio
from adafruit_motor 

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

# Initialize Neopixel RGB LEDs
pixels = neopixel.NeoPixel(board.GP18, 2)
pixels.fill(0)

class UltrasonicSensor:
    """A class to manage an ultrasonic sensor like the HC-SR04."""
    
    def __init__(self, trig_pin, echo_pin):
        # Set up the trigger pin (output)
        self.trig = digitalio.DigitalInOut(GP7)
        self.trig.direction = digitalio.Direction.OUTPUT
        self.trig.value = False
        
        # Set up the echo pin (input)
        self.echo = digitalio.DigitalInOut(GP28)
        self.echo.direction = digitalio.Direction.INPUT

    def get_distance(self):
        """Measures the distance using the ultrasonic sensor."""
        
        # Send a trigger pulse (10 microseconds high)
        self.trig.value = True
        time.sleep(0.00001)  # 10 microseconds
        self.trig.value = False

        # Wait for the echo to go high (start of echo)
        while not self.echo.value:
            pass

        # Record the start time
        start_time = time.monotonic()

        # Wait for the echo to go low (end of echo)
        while self.echo.value:
            pass

        # Record the end time
        end_time = time.monotonic()

        # Calculate the duration of the echo pulse
        duration = end_time - start_time

        # Speed of sound is approximately 343 meters per second or 0.0343 cm/µs.
        # Divide by 2 because the sound travels to the object and back.
        distance_cm = (duration * 34300) / 2

        return distance_cm


# Example usage:

# Define pins for the ultrasonic sensor (adjust as needed)
TRIG_PIN = board.GP7  # Replace with the correct pin for your microcontroller
ECHO_PIN = board.GP28  # Replace with the correct pin for your microcontroller

# Create an instance of the UltrasonicSensor
ultrasonic = UltrasonicSensor(TRIG_PIN, ECHO_PIN)

# Loop to continuously measure distance
while True:
    distance = ultrasonic.get_distance()
    print(f"Distance: {distance:.2f} cm")
    time.sleep(1)  # Measure distance every second

LEDS(GP0).value = True

