import picamera
import datetime


class PhotoHandler:
    def get_photo(self):
        with picamera.PiCamera() as camera:
            name = datetime.datetime.now()
            camera.capture(f"/home/pi/Desktop/ServerFiles/Pictures/{name}.jpeg")
            return 'Picture taken', 200