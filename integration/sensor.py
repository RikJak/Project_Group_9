import RPi.GPIO as GPIO
import time
import datetime
class Sensor():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.pir = 8
        GPIO.setup(self.pir,GPIO.IN)
        time.sleep(2)
    
    def run_sensor(self):
        try:
            while True:
                if GPIO.input(self.pir) == True:
                    print(f"motion detected at: {datetime.datetime.now()}")
                    time.sleep(5)

        finally:
            GPIO.cleanup()