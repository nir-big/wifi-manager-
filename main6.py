import time
from WiFiManager4 import WiFiManager
from MotorController3 import MotorController
from HTTPServer2 import HTTPServer
from UltrasonicSensor2 import UltrasonicSensor
from machine import Pin, SPI
from ili9341 import color565
from GolanDisplay import GolanDisplay
import _thread

def main():
    SSID = 'robotics'  # Replace with your Wi-Fi SSID
    PASSWORD = 'arduino1'  # Replace with your Wi-Fi password
    motor_pins = {
        'input1': 18,
        'input2': 5,
        'enable': 23,
        'input3': 15,
        'input4': 17,
        'enable2': 16
    }

    # SPI Configuration for the display
    spi = SPI(1, baudrate=20000000, sck=Pin(14), mosi=Pin(13), miso=Pin(19))
    cs = Pin(33)
    dc = Pin(12)
    rst = Pin(27)

    # Initialize display
    display = GolanDisplay(spi, cs, dc, rst)
    display.display.clear(color565(255, 255, 255))  # White background

    # Initialize Wi-Fi Manager and connect to Wi-Fi
    wifi_manager = WiFiManager(SSID, PASSWORD)
    ip_address = wifi_manager.connect()

    if ip_address:
        print(f"ESP32 IP Address: {ip_address}")
        
        # Initialize MotorController and HTTPServer
        motor_controller = MotorController(motor_pins)
        http_server = HTTPServer(motor_controller)
        sensor = UltrasonicSensor(trig_pin=4, echo_pin=2)  # Correct instantiation

        # Start the HTTP server in a separate thread if needed
        _thread.start_new_thread(http_server.start, (ip_address,))

        # Main loop to monitor the ultrasonic sensor
        while True:
            # Measure the distance
            display.display.clear(color565(255, 255, 255))  # Reset to white background
            
            distance = sensor.measure_distance()
            print(f"Measured Distance: {distance}")  # Debugging line to check distance

            # Display text based on measurement
            if distance != -1:
                distance_text = f"{distance:.1f} CM"  # Format distance with one decimal place
            else:
                distance_text = "OUT OF RANGE"















            # Clear the previous text
            display.display.fill_rectangle(50, 100, 240, 50, color565(255, 255, 255))  # White background for the area

            # Debugging output to the console
            print(f"Displaying text: {distance_text}")

            # Draw the new distance text
            display.draw_vertical_text(50, 160, distance_text, color565(0, 0, 0), scale=3, spacing=2)

            # Motor control logic if distance is less than 10 cm
            if distance < 10:
                motor_controller.rotate_left()
                while sensor.measure_distance() < 10:
                    time.sleep(0.1)
                motor_controller.stop()

            time.sleep(0.1)  # Adjust the delay as needed
    else:
        print("Unable to get IP address, exiting...")

if __name__ == "__main__":
    main()
