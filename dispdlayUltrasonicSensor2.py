from machine import Pin, SPI
from ili9341 import color565
from GolanDisplay import GolanDisplay
import time
from UltrasonicSensor2 import UltrasonicSensor  # Assuming you named the ultrasonic class in another file

def main():
    # SPI Configuration
    spi = SPI(1, baudrate=20000000, sck=Pin(14), mosi=Pin(13), miso=Pin(19))
    cs = Pin(33)
    dc = Pin(12)
    rst = Pin(27)
    
    # Initialize display
    display = GolanDisplay(spi, cs, dc, rst)
    display.display.clear(color565(255, 255, 255))  # White background

    # Initialize ultrasonic sensor
    trig_pin = 4
    echo_pin = 2
    sensor = UltrasonicSensor(trig_pin, echo_pin)

    while True:
        # Measure the distance
        display.display.clear(color565(255, 255, 255))  # Reset to white background
        
        distance = sensor.measure_distance()

        # Display text based on measurement
        if distance != -1:
            distance_text = f"{distance:.1f} CM"  # Format distance with one decimal place
        else:
            distance_text = "OUT OF RANGE"

        # Clear the previous text
        display.display.fill_rectangle(50, 100, 240, 50, color565(255, 255, 255))  # White background for the area
        
        # Draw the new distance text
        display.draw_vertical_text(50, 160, distance_text, color565(0, 0, 0), scale=3, spacing=2)

        time.sleep(0.05)  # Update every 0.5 seconds

if __name__ == "__main__":
    main()
