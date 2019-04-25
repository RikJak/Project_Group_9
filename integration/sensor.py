# import RPi.GPIO as GPIO
# import time
# import datetime
import requests
import threading
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, Response, request, abort
import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/integration")
from sensor_pi import SensorPi

#Setup of sensor
# GPIO.setmode(GPIO.BOARD)
# pir = 8
# GPIO.setup(pir,GPIO.IN)
# time.sleep(2)

#Variables
number_of_args=len(sys.argv)
server_IP= sys.argv[3]

#Setup of server
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

#Sensor setup
SensorPi = SensorPi(server_IP)

@app.before_request
def limit_remote_addr():
    if  number_of_args >1:
        client_ip = sys.argv[1]
        PORT = sys.argv[2]
        

    if request.remote_addr != client_ip:
         abort(403)

@app.route('/sensor_on' methods = ['POST'])
def sensor_on(self):
    
@app.route('/sensor_off', methods = ['POST'])
def sensor_off(self):

if __name__ == '__main__':
    global server_IP
    app.run(host=server_IP, port =PORT, debug=True, threaded=True)
