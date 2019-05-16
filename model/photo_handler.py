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
        webserver_address= 'url'
        self.webserver_connection = WebserverConnection()

    def take_photo(self):
        """
        Takes a photo and saves it to a file using the time as a name.
        @return: name of file containing photo
        """
        with picamera.PiCamera() as camera:
            name = datetime.datetime.now()
            filename = f"/home/pi/Desktop/ServerFiles/Pictures/{name}.jpeg"
            camera.camera.PiCamera(rotation=180,resolution=(1920,1080))  
            camera.capture(filename)
        return filename

    def get_photo(self):
        """
        Takes a photo
        @output: {'msg':filename},200
        """
        res = self.take_photo()
        return json.dumps({'msg':res}), 200
    
    def get_motion_photo(self):
        """
        Takes a photo and sends it to the webserver.
        @output:  {'msg':filename},200
        """
        filename = self.take_photo()
        res = self.webserver_connection.send_photo(filename)
        return json.dumps({'msg':res}), 200