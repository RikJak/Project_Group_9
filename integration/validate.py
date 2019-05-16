#This is a validator

import requests
import json
import os,sys

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../")
import configFile
config = configFile.Config()
server_address = config.get_webserver_IP() 
#server_address = 'http://g9.apic.eu-gb.mybluemix.net/'
class Validate():


    def validate_user(self,email,api_key):
        """
        Takes the provided user details and sends them to the webserver for validation.
        If the returned JSON contains 'true' the user will be considered valid
        @input: email,api_key
        @output: boolean
        """
        print(api_key)
        print(email)

        content = {'email':email,'api_key':api_key}
        content = json.dumps(content)
        headers = {"Content-Type":"application/json"}
        r = requests.post(f'http://{server_address}/api/user/validate_user', data = content,headers = headers,verify=False)

        msg = json.loads(r.content)
        print(msg)

        if(msg['result']=='true'):
            return True


        return False #Change when it's working
    
