import requests
import json
from config import Config

class WebserverConnection:
    def __init__(self):

        config = Config()
        self.webserver_address= config.get_webserver_IP()

    def change_IP(self,server_IP,MAC):
        content = {'server_IP':server_IP,'MAC_address':MAC}
        content = json.dumps(content)
        headers = {"Content-Type":"application/json"}
        #address will be given by the api
        r = requests.post(f"http://{self.webserver_address}/api/camera/update_ip", data = content,headers = headers,verify=False)
        if(r.status_code == 200):
            return True
        return False
    def send_photo(self,filename):
        files = {'media' : open(filename,'rb')}
        r = requests.post(f"http://{self.webserver_address}/api/user/notify", files = files) # url needs to be changed!
        if(r.status_code == 200):
            return True
        return False
        