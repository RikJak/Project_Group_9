import os 
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")

from device import Device
import json

class DeviceInfoHandler:
    def __init__(self):
        self.device = Device()

    def get_MAC_address(self):
        MAC_address = self.device.get_MAC_address()
        return MAC_address
    
    def get_IP_address(self):
        IP_address = self.device.get_IP_address()
        return IP_address   