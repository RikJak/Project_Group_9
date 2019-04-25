import picamera
import datetime
import json
import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")
from webserver_connection import WebserverConnection

class PhotoHandler:
    def __init__(self):
        self.webserver_connection = WebserverConnection()

    def take_photo(self):
        with picamera.PiCamera() as camera:
            name = datetime.datetime.now()
            filename = f"/home/pi/Desktop/ServerFiles/Pictures/{name}.jpeg"
            camera.capture(filename)
        return filename

    def get_photo(self):
        self.take_photo()
        return json.dumps({'msg':'Picture taken'}), 200
    
    def get_motion_photo(self):
        filename = self.take_photo()
        self.webserver_connection.send_photo(filename)
        return json.dumps({'msg':'Picture taken and sent'}), 200