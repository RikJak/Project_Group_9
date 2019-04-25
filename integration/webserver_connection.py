import requests
import json
class WebserverConnection:
    def __init__(self,webserver_address):
        self.webserver_address= webserver_address

    def change_IP(self,server_IP,MAC):
        # content = {'server_IP':server_IP,'MAC_address':MAC}
        # content = json.dumps(content)
        # headers = {"Content-Type":"application/json"}
        # address will be given by the api
        # r = requests.post(f"{self.websever_address}/api/something", data = content,headers = headers,verify=False) # needs to be changed!
        # if(r.status_code == 200):
        return True
    
    def send_photo(self,filename):
        # files = {'media' : open(filename,'rb')}
        # r = requests.post(f"{self.webserver_address}/api/something", files = files) # url needs to be changed!
        return True