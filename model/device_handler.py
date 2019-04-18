import os 
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")

#from device import Device
import json
from device_info_handler import DeviceInfoHandler
from file_writer import FileWriter


class DeviceHandler:
    def __init__(self):
        self.device = DeviceInfoHandler()
        self.file = FileWriter()
    
    def register_device(self,webserver_IP):
        local_IP = self.device.get_IP_address()
        self.file.make_config({'local_IP': local_IP,'webserver_IP':webserver_IP})
