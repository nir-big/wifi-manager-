from machine import Pin, time_pulse_us
import time

class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin, timeout=30000):
        """
        Initializes the ultrasonic sensor with the specified trigger and echo pins.
        :param trig_pin: GPIO pin connected to the Trigger.
        :param echo_pin: GPIO pin connected to the Echo.
        :param timeout: Maximum time in microseconds to wait for the echo pulse (default 30ms).
        """
        self.trigger = Pin(trig_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        self.timeout = timeout

        # Ensure the trigger pin starts LOW
        self.trigger.off()

    def measure_distance(self):
        """
        Measures the distance using the ultrasonic sensor and returns it in centimeters.
        :return: Distance in cm, or -1 if the reading is out of range or invalid.
        """
        # Send a 10µs pulse to trigger the sensor
        self.trigger.off()
        time.sleep_us(2)
        self.trigger.on()
        time.sleep_us(10)
        self.trigger.off()

        # Measure the time for the echo pulse
        duration = time_pulse_us(self.echo, 1, self.timeout)

        # Calculate distance
        if duration > 0:
            distance = (duration * 0.0343) / 2
            return distance
        else:
            return -1  # Indicates a timeout or invalid reading

# Example usage
if __name__ == "__main__":
    # Configure the pins for the ultrasonic sensor
    TRIG_PIN = 4  # GPIO pin for Trigger
    ECHO_PIN = 2  # GPIO pin for Echo

    # Create an instance of the UltrasonicSensor class
    sensor = UltrasonicSensor(TRIG_PIN, ECHO_PIN)

    # Main loop
    while True:
        distance = sensor.measure_distance()
        if distance == -1:
            print("Out of range or no object detected!")
        else:
            print(f"Distance: {distance:.2f} cm")
        time.sleep(0.5)  # Delay between readings

