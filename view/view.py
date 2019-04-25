import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../controller")
from flask_cors import CORS, cross_origin
from contr import Controller
from flask import Flask, redirect, url_for, request
import json

controller = Controller()
SERVER_IP = controller.get_IP_address()
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
 
print(f"IP is correct : {controller.verify_IP(SERVER_IP)}")
def limit_to_raspberry():
   if request.remote_addr != SERVER_IP:
      abort(403)

@app.route('/',methods = ['POST'])
def request_handler():
   email = request.args.get('email')
   api_key = request.args.get('api_key')
   client_IP = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
   return controller.set_up_stream(email,api_key,client_IP,SERVER_IP)  

@app.route('/reboot', methods = ['POST'])
def request_reboot():
   email = request.args.get('email')
   api_key = request.args.get('api_key')
   return controller.reboot(email,api_key)

@app.route('/photo', methods = ['POST'])
def get_photo():
   limit_to_raspberry()
   return controller.get_photo()

@app.route('/motion_photo', methods = ['POST'])
def get_motion_photo():
   limit_to_raspberry()
   return controller.get_motion_photo()

@app.route('/get_MAC', methods = ['POST'])
def get_MAC():
   return json.dumps({'MAC_address': controller.get_MAC_address()})

@app.route('/get_IP', methods = ['POST'])
def get_IP():
   return json.dumps({'IP_address':controller.get_IP_address()})

@app.route('/register', methods = ['POST'])
def register():
   server_IP =request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
   return controller.register(server_IP)

@app.route('/start_sensor',methods = ['POST'])
def start_sensor():
   email = request.args.get('email')
   api_key = request.args.get('api_key')
   client_IP = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
   return controller.start_sensor(email,api_key,client_IP,SERVER_IP)

if __name__ == '__main__':
   app.run(host = SERVER_IP, debug=False)
