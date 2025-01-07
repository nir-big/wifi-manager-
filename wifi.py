import network
import time

class WiFiManager:
    def __init__(self, SSID, PASSWORD):
        self.SSID = SSID
        self.PASSWORD = PASSWORD

    def connect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.SSID, self.PASSWORD)
        print("Connecting to Wi-Fi...")

        attempt = 0
        while not wlan.isconnected() and attempt < 20:
            time.sleep(1)
            print(".", end="")
            attempt += 1

        if wlan.isconnected():
            print("\nConnected to Wi-Fi!")
            print("IP Address:", wlan.ifconfig()[0])
            return wlan.ifconfig()[0]  # Return IP address
        else:
            print("\nFailed to connect to Wi-Fi.")
            return None

