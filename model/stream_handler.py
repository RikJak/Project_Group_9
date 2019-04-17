import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")

from validate import Validate
# import picamera
# from camera_pi import Camera
# import logging
# import socketserver
# from streaming_handler import StreamingHandler
# from streaming_output import StreamingOutput
# from threading import Condition
# from http import server
import json
from subprocess import call
from picamera import PiCamera
import random
PORT = 8000
SERVER_IP = '130.237.215.167'
class StreamHandler:
    def __init__(self):
        self.validate= Validate()
        

    def set_up_stream(self,email,api_key,client_ip):
        valid = self.validate.validate_user(email,api_key)
        valid = True # this will ba taken away when the validate server is up and working
        if (valid):
            # subprocess.call(['python3', '/home/Project_Group_9/model/video_stream.py', str(client_ip), str(PORT)])
            # call(f"python3 /home/Project_Group_9/model/video_stream.py {client_ip} {PORT}", shell=True)
            # run("/home/Project_Group_9/model/video_stream.py", client_ip, PORT)
            start_command = f"sudo python3 /home/Project_Group_9/model/video_stream.py {client_ip} {PORT} &"
            os.system(start_command)
            return json.dumps({'port':PORT, 'server_ip': SERVER_IP})
        return '', 403

    def reboot(self,email,api_key):
        valid = self.validate.validate_user(email,api_key)
        valid = True # will be removed if real validation is made!
        if (valid):
            os.system('sudo reboot')
            return {'msg': 'Rebooting'}
        return '', 403
    
    def get_photo(self):
        with picamera.PiCamera() as camera:
        name =random.randint(1,99999999999999999999)
        camera.capture(f"/home/pi/Desktop/Pictures/{name}.jpeg")
        return 'Picture taken', 200

    # def camera_init(self):
    #     return PiCamera()