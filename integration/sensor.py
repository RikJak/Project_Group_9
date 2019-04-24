import RPi.GPIO as GPIO
import time
import datetime
GPIO.setmode(GPIO.BOARD)
pir = 8
GPIO.setup(pir,GPIO.IN)
time.sleep(2)
print("Sensor on")
try:
    while True:
        if GPIO.input(pir):
            print(f"motion detected at: {datetime.datetime.now()}")
            time.sleep(5)

finally:
    GPIO.cleanup()
