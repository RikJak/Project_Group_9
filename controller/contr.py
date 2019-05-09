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
        """
        Starts a stream server.
        @input: api_key; client_IP; server_IP
        @output: Json containing ip address and port of video stream
        """
        return self.handler.set_up_stream(email,api_key,client_IP,server_IP)

    def reboot(self, email,api_key):
        """
        Reboots the RaspberryPi
        @input email, api-key
        @output: None
        """
        return self.handler.reboot(email,api_key)

    def get_photo(self):
        """
        Takes a photo
        @output:  {'msg':filename}
        """
        return self.photo_handler.get_photo()

    def get_motion_photo(self):
        """
        Takes a photo and sends it to the webserver
        @output:  {'msg':filename}
        """
        return self.photo_handler.get_motion_photo()

    def get_MAC_address(self):
        """
        @output: The MAC address of the device
        """
        return self.device_info_handler.get_MAC_address()

    def get_IP_address(self):
        """
        @output: The IP address of the device
        """
        return self.device_info_handler.get_IP_address()

    def register(self,server_IP):
        """
        Registers the device to use the provided IP as the webserver used for validation, etc.
        @output: {'MAC_address:0x....}

        """
        return self.device_handler.register_device(server_IP)

    def verify_IP(self,server_IP):
        """
        Verifies that the stored local IP is the same as the current one
        @output: boolean
        """
        return self.device_handler.verify_IP(server_IP)

    def start_sensor(self,email,api_key,client_IP,device_IP):
        """¨
        Starts the sensor server
        @input: email,api_key,client_IP, device_IP
        @output: {'port':PORT, 'server_ip': server_IP},200/403 if using invalid credentials
        """
        return self.sensor_handler.start_sensor(email,api_key,client_IP,device_IP)