import time
from WiFiManager4 import WiFiManager
from MotorController3 import MotorController
from HTTPServer2 import HTTPServer
from UltrasonicSensor2 import UltrasonicSensor  # Correct import

def main():
    SSID = 'robotics'  # Replace with your Wi-Fi SSID
    PASSWORD = 'arduino1'  # Replace with your Wi-Fi password
    motor_pins = {
        'input1': 27,
        'input2': 33,
        'enable': 19,
        'input3': 12,
        'input4': 13,
        'enable2': 14
    }

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
        import _thread
        _thread.start_new_thread(http_server.start, (ip_address,))

        # Main loop to monitor the ultrasonic sensor
        while True:
            distance = sensor.measure_distance()
            print(f"Distance: {distance:.2f} cm")

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
