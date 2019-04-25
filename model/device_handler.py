import os 
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")

#from device import Device
import json
from device_info_handler import DeviceInfoHandler
from config import Config
from webserver_connection import WebserverConnection


class DeviceHandler:
    def __init__(self):
        self.device = DeviceInfoHandler()
        self.file = Config()
        self.webserver_connection = WebserverConnection()
    
    def register_device(self,webserver_IP):
        local_IP = self.device.get_IP_address()
        self.file.make_config({'local_IP': local_IP,'webserver_IP':webserver_IP})
        MAC = self.device.get_MAC_address()
        return json.dumps({'MAC_Address': MAC})

    def verify_IP(self, server_IP):
        local_IP = self.file.get_local_IP()
        if server_IP != local_IP:
            print(f"local: {local_IP} server {server_IP}")
            MAC = self.device.get_MAC_address()
            web_IP = self.file.get_webserver_IP()
            self.register_device(web_IP)
            return self.webserver_connection.change_IP(server_IP,MAC)
        return True

            
