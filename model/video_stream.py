import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")
from flask import Flask, render_template, Response, request, abort
from camera_pi import Camera
import json
from validate import Validate
from flask_cors import CORS, cross_origin
# Raspberry Pi camera module (requires picamera package)
RES_X=640
RES_Y=480
CAMERA = Camera(480,360)
number_of_args=len(sys.argv)
client_ip = sys.argv[1]
PORT = sys.argv[2]

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown_stream', methods = ['POST'])
def shutdown_stream():
    if request.method == 'POST':
        valid = True
        # validate = Validate()
        # email = request.args.get('email')
        # api_key = request.args.get('api_key')
        # valid = validate.validate_user(email,api_key)
        if (valid):
            shutdown_server()
            return ':ok', 200
        return '', 403

# @app.before_request
def limit_remote_addr():
    if request.remote_addr != client_ip:
        abort(403)

# @app.route('/')
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed(CAMERA=None):
    limit_remote_addr()
    global RES_X
    global RES_Y    
    if CAMERA is None:
        CAMERA = Camera(RES_X,RES_Y)
    print(f"The resolution is {CAMERA.get_res()}")
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(CAMERA), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/settings', methods = ['POST','GET'])
def request_handler():
    limit_remote_addr()
    if request.method == 'POST' or request.method == 'GET':
        global RES_X
        global RES_Y
        RES_X = request.args.get('res_x')
        RES_Y = request.args.get('res_y')
        CAMERA = Camera(RES_X,RES_Y)
        resolution=(f"{RES_X}x{RES_Y}")
        video_feed(CAMERA)
        return json.dumps({'msg':'ok','res':resolution})



if __name__ == '__main__':
    server_IP= sys.argv[3]
    app.run(host=server_IP, port =PORT, debug=False, threaded=True)
