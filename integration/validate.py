#This is a validator

import requests
import json
from config import Config
config = Config()
server_address = Config.get_webserver_IP()#'https://g9.apic.eu-gb.mybluemix.net/'
class Validate:


    def validate_user(self,email,api_key):
        """This method contacts the cloud server to verify that the user is valid. If status code 200 is returned the user is valid, and the function returns true
        @Rikard
        """
        content = {'email':email,'api_key':api_key}
        content = json.dumps(content)
        headers = {"Content-Type":"application/json"}
        r = requests.post(f'{server_address}/api/user/validate_user', data = content,headers = headers,verify=False)
        #msg = r.content

        if(r.status_code == 200):
            return True


        return False #Change when it's working
    
