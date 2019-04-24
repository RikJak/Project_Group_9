import requests
import json
class WebserverConnection:
    def change_IP(self,server_IP,MAC):
        # content = {'server_IP':server_IP,'MAC_address':MAC}
        # content = json.dumps(content)
        # headers = {"Content-Type":"application/json"}
        # address will be given by the api
        # r = requests.post('https://webserver-toolchain-noisy-possum.eu-gb.mybluemix.net/api/', data = content,headers = headers,verify=False)
        # if(r.status_code == 200):
        return True