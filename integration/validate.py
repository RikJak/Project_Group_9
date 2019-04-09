#This is a validator

import requests
import json
class Validate:
    TEST_USER = 'mhild@kth.se'
    TEST_KEY = 'Db-fNOW05Mwe4dcN8AhRdNPRSCtQi8PUInt5Uy3Q'
    def __init__(self):
        self.test()
    def validate_user(self,email,api_key):
        """This method contacts the cloud server to verify that the user is valid
        @Rikard
        """
        content = {'email':email,'api_key':api_key}
        content = json.dumps(content)
        headers = {"Content-Type":"application/json"}
        print(content)
        r = requests.post('http://g9.apic.eu-gb.mybluemix.net/api/user/validate_user', data = content,headers = headers,verify=False)
        print(r.content)
        return r

    def test(self):
        """TEMPORARY TEST METHOD
        """
        print(self.validate_user(self.TEST_USER,self.TEST_KEY))

r = Validate()