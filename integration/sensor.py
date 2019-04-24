import RPi.GPIO as GPIO
import time
import datetime
import requests
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, Response, request, abort

#Setup of sensor
GPIO.setmode(GPIO.BOARD)
pir = 8
GPIO.setup(pir,GPIO.IN)
time.sleep(2)

#Variables
number_of_args=len(sys.argv)
server_IP= sys.argv[3]

#Setup of server
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.before_request
def limit_remote_addr():
    if  number_of_args >1:
        client_ip = sys.argv[1]
        PORT = sys.argv[2]
        

    if request.remote_addr != client_ip:
         abort(403)
@app.route('/sensor_on' methods = ['POST'])
def start_sensor(self):
    print("Sensor on")
    try:
        while True:
            if GPIO.input(pir):
                print(f"motion detected at: {datetime.datetime.now()}")
                global server_IP
                request_address = f"http://{server_IP}:5000/photo"
                r = requests.post(request_address,verify=False)
                if(r.status_code == 200):
                    print("Photo taken!")
                time.sleep(4)

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    global server_IP
    app.run(host=server_IP, port =PORT, debug=True, threaded=True)
