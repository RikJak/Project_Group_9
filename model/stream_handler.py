import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")

from validate import Validate
import picamera
from camera_pi import Camera
import logging
import socketserver
from streaming_handler import StreamingHandler
from streaming_output import StreamingOutput
from threading import Condition
from http import server


from flask import Flask, render_template, Response
from camera_pi import Camera

PORT = 8001
SERVER_IP = '130.237.215.167'

app = Flask(__name__)
@app.route('/')
# def index():
#     """Video streaming home page."""
#     return render_template('index.html')
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host=SERVER_IP, port = PORT, debug=True, threaded=True)

# class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
#     allow_reuse_address = True
#     daemon_threads = True
    
# class StreamHandler:
#     def __init__(self):
#         self.validate= Validate()

#     def set_up_stream(self,email,api_key,client_ip):
#         valid = self.validate.validate_user(email,api_key)

#         if(valid):

#             with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
#                 output = StreamingOutput()
#                 #Uncomment the next line to change your Pi's Camera rotation (in degrees)
#                 #camera.rotation = 90
#                 camera.start_recording(output, format='mjpeg')
#             try:
#                 address = ('', PORT)
#                 server = StreamingServer(address, StreamingHandler)
#                 server.serve_forever()
#             finally:
#                 camera.stop_recording()

