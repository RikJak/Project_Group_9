import RPi.GPIO as GPIO
import time
import datetime
GPIO.setmode(GPIO.BCM)
pir = 8
GPIO.setup(pir,GPIO.IN)
time.sleep(2)
run_sensor()
    
def run_sensor():
    try:
        while True:
            if GPIO.input(pir):
                print(f"motion detected at: {datetime.datetime.now()}")
                time.sleep(5)

    finally:
        GPIO.cleanup()
