import RPi.GPIO as GPIO
import time
import datetime
import requests
import threading

class SensorPi():
    thread = None

    def __init__(self,server_IP):
        GPIO.setmode(GPIO.BOARD)
        self.pir = 8
        GPIO.setup(self.pir,GPIO.IN)
        time.sleep(2)
        self.server_IP = server_IP
        self.sensor_running = True
        self.initiate()

    def initiate(self):
        if SensorPi.thread is None:
            # start background thread
            SensorPi.thread = threading.Thread(target=self._sensor_thread)
            SensorPi.thread.start()
    
    def _sensor_thread(self):
        print("Sensor on")
        try:

            while self.sensor_running:
                if GPIO.input(self.pir):
                    print(f"motion detected at: {datetime.datetime.now()}")
                    request_address = f"http://{self.server_IP}:5000/photo"
                    r = requests.post(request_address,verify=False)
                    if(r.status_code == 200):
                        print("Photo taken!")
                    time.sleep(4)

        finally:
            GPIO.cleanup()
    
    def sensor_off(self):
        self.sensor_running= False
    
    def sensor_on(self):
        self.sensor_running = True
        self.initiate()