#This is a stream handler
import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../model")
from stream_handler import StreamHandler
from photo_handler import PhotoHandler
from device_info_handler import DeviceInfoHandler
from device_handler import DeviceHandler
from sensor_handler import SensorHandler

class Controller:
    def __init__(self):
        self.handler = StreamHandler()
        self.photo_handler = PhotoHandler()
        self.device_info_handler = DeviceInfoHandler()
        self.device_handler = DeviceHandler()
        self.sensor_handler = SensorHandler()
        
    def set_up_stream(self,email,api_key,client_IP,server_IP):
        return self.handler.set_up_stream(email,api_key,client_IP,server_IP)

    def reboot(self, email,api_key):
        return self.handler.reboot(email,api_key)

    def get_photo(self):
        return self.photo_handler.get_photo()

    def get_MAC_address(self):
        return self.device_info_handler.get_MAC_address()

    def get_IP_address(self):
        return self.device_info_handler.get_IP_address()

    def register(self,server_IP):
        return self.device_handler.register_device(server_IP)

    def verify_IP(self,server_IP):
        return self.device_handler.verify_IP(server_IP)

    def start_sensor(self,email,api_key,client_IP,server_IP):
        return self.sensor_handler.start_sensor(email,api_key,client_IP,server_IP)