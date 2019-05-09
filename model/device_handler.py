import os 
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")

#from device import Device
import json
from device_info_handler import DeviceInfoHandler
from config import Config
from webserver_connection import WebserverConnection
HARDCODED_WEB_IP = 'g9.apic.eu-gb.mybluemix.net/'#Temporary fix


class DeviceHandler:
    def __init__(self):
        self.device = DeviceInfoHandler()
        self.file = Config()
        self.webserver_connection = WebserverConnection()
    
    def register_device(self,webserver_IP):
        """
        Gets the local IP and then creates a config file using the provided webserver IP address and the local IP
        @input: IP to the webserver
        @output: The MAC address of the device
        """
        local_IP = self.device.get_IP_address()
        self.file.make_config({'local_IP': local_IP,'webserver_IP':HARDCODED_WEB_IP})#Fix hardcode
        MAC = self.device.get_MAC_address()
        return json.dumps({'MAC_Address': MAC})

    def verify_IP(self, server_IP):
        """
        Verifies that the current IP of the device matches the one that was provided to the webserver.
        If they do not match the config will be updated and the new device IP will be sent to the webserver.
        @input: the current IP of the device
        @output: boolean
        """
        local_IP = self.file.get_local_IP()
        if server_IP != local_IP:
            print(f"local: {local_IP} server {server_IP}")
            MAC = self.device.get_MAC_address()
            web_IP = self.file.get_webserver_IP()
            self.register_device(HARDCODED_WEB_IP)#Fix hardcode
            return self.webserver_connection.change_IP(server_IP,MAC)
        return True

            
