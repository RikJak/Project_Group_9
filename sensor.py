import requests
import threading
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, Response, request, abort
import os
import sys
import json
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/integration")
from sensor_pi import SensorPi

#Variables
number_of_args=len(sys.argv)
if  number_of_args >1:
    server_IP= sys.argv[3]
    PORT = sys.argv[2]
    client_ip = sys.argv[1]

#Setup of server
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

#Sensor setup
sensor_pi = None

@app.before_request
def limit_remote_addr():
    if request.remote_addr != client_ip:
         abort(403)

@app.route('/sensor_on', methods = ['POST'])
def sensor_on():
    global sensor_pi
    sensor_pi = SensorPi(server_IP)
    sensor_pi.sensor_on()
    return json.dumps({'msg':'Sensor turned on'})

@app.route('/sensor_off', methods = ['POST'])
def sensor_off():
    global sensor_pi
    sensor_pi.sensor_off()
    return json.dumps({'msg':'Sensor turned off'})

if __name__ == '__main__':
    app.run(host=server_IP, port=PORT, debug=True, threaded=True)
    