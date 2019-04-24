import RPi.GPIO as GPIO
import time
import datetime
import requests
GPIO.setmode(GPIO.BOARD)
pir = 8
GPIO.setup(pir,GPIO.IN)
time.sleep(2)
print("Sensor on")
try:
    while True:
        if GPIO.input(pir):
            print(f"motion detected at: {datetime.datetime.now()}")
            r = requests.post('http://130.237.215.167:5000/photo',{"Content-Type":"application/json"},verify=False)
            if(r.status_code == 200):
                print("Photo taken!")
            time.sleep(4)

finally:
    GPIO.cleanup()
