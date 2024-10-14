import time
import board
import digitalio
import pulseio

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


# Example usage:

# Define pins for the ultrasonic sensor (adjust as needed)
TRIG_PIN = board.GP18  # Replace with the correct pin for your microcontroller
ECHO_PIN = board.GP19  # Replace with the correct pin for your microcontroller

# Create an instance of the UltrasonicSensor
ultrasonic = UltrasonicSensor(TRIG_PIN, ECHO_PIN)

# Loop to continuously measure distance
while True:
    distance = ultrasonic.get_distance()
    print(f"Distance: {distance:.2f} cm")
    time.sleep(1)  # Measure distance every second
