import time
import board
import digitalio

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


class UltrasonicSensor:
    """A class to manage an ultrasonic sensor like the HC-SR04."""
    
    def __init__(self, trig_pin, echo_pin):
        # Set up the trigger pin (output)
        self.trig = digitalio.DigitalInOut(trig_pin)
        self.trig.direction = digitalio.Direction.OUTPUT
        self.trig.value = False
        
        # Set up the echo pin (input)
        self.echo = digitalio.DigitalInOut(echo_pin)
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


def control_leds_by_distance(distance):
    """Turn off LEDs based on the distance measured by the ultrasonic sensor."""
    # Assume distance between 5 cm and 20 cm
    if distance < 5:
        distance = 5  # Set a lower bound
    elif distance > 20:
        distance = 20  # Set an upper bound

    # Map the distance to the number of LEDs to turn off (reverse logic)
    num_leds_off = int(((distance - 5) / 15) * len(LEDS))

    # Turn off the calculated number of LEDs
    for i in range(len(LEDS)):
        if i < num_leds_off:
            LEDS[i].value = False  # Turn off the LED
        else:
            LEDS[i].value = True  # Keep the LED on


# Define pins for the ultrasonic sensor
TRIG_PIN = board.GP7  # Adjust the pin to your setup
ECHO_PIN = board.GP28  # Adjust the pin to your setup

# Create an instance of the UltrasonicSensor
ultrasonic = UltrasonicSensor(TRIG_PIN, ECHO_PIN)

# Turn on all LEDs at the beginning
for led in LEDS:
    led.value = True

# Loop to continuously measure distance and control LEDs
while True:
    distance = ultrasonic.get_distance()
    print(f"Distance: {distance:.2f} cm")
    control_leds_by_distance(distance)
    time.sleep(0.5)  # Measure distance every 0.5 second
