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
import video_stream
import json


PORT = 8001
SERVER_IP = '130.237.215.167'
class StreamHandler:
    def __init__(self):
        self.validate= Validate()

    def set_up_stream(self,email,api_key,client_ip):
        valid = self.validate.validate_user(email,api_key)
        valid = True
        if (valid):

            os.system('sudo python3 /home/Project_Group_9/model/video_stream.py &')
            # video_stream.start_stream(client_ip,PORT)
            return json.dumps({'port':PORT, 'server_ip': SERVER_IP})
        return '', 403
            

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

