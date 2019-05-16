import requests
import json
import configFile
from device import Device
from flask import jsonify

class WebserverConnection:
    def __init__(self):

        config = configFile.Config()
        self.webserver_address= config.get_webserver_IP()

    def change_IP(self,server_IP,MAC):
        """
        Sends the current ip and MAC address in a JSON to the webserver.
        If the server returns http code 200 True will be returned.
        @input: device_IP, MAC
        @output: boolean
        """
        content = {'server_IP':server_IP,'MAC_address':MAC}
        content = json.dumps(content)
        headers = {"Content-Type":"application/json"}
        #address will be given by the api
        r = requests.post(f"http://{self.webserver_address}/api/camera/update_ip", data = content,headers = headers,verify=False)
        if(r.status_code == 200):
            return True
        return False
    def send_photo(self,filename):
        """
        Sends a file to the webserver in a JSON.
        Will return True if status code 200 is returned from the webserver.
        @input: filname of the file to be sent
        @output: boolean
        """
        device = Device()
        mc = device.get_MAC_address()
        mac= f"{mc}"
        files = {"media" : open(filename,'rb')}
        print(mac)
        r = requests.post(f"http://{self.webserver_address}/api/user/notify", data = {"MAC_address":mac}, files = files) 
        msg = r.text
        print(msg)
        if(r.status_code == 200):
            return True
        return False
        