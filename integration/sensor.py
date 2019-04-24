import RPi.GPIO as GPIO
import time
class Sensor:
    def __init__(self):
        self.pir = 8
        GPIO.setup(self.pir,GPIO.IN)
        time.sleep(2)
    
    def run_sensor(self):
        try:
            while True:
                if GPIO.input(self.pir) == True:
                    print("motion detected")

        finally:
            GPIO.cleanup()