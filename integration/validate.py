#This is a validator

import requests
import json
class Validate:

    def validate_user(self,email,api_key):
        """This method contacts the cloud server to verify that the user is valid. If status code 200 is returned the user is valid, and the function returns true
        @Rikard
        """
        content = {'email':email,'api_key':api_key}
        content = json.dumps(content)
        headers = {"Content-Type":"application/json"}
        r = requests.post('https://webserver-toolchain-noisy-possum.eu-gb.mybluemix.net/api/user/validate_user', data = content,headers = headers,verify=False)
        #msg = r.content

        if(r.status_code == 200):
            return True


        return True #Change when it's working
    
