import unittest
import os
import sys
import requests
import json

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../")
SERVER_IP_PORT = '130.237.215.167:5000'

class TestView(unittest.TestCase):

    def test_post_request(self):
        content = {'email':'email','api_key':'api_key'}
        content = json.dumps(content)
        r = requests.post(SERVER_IP_PORT, data = content,verify=False)
        response = r.status_code
        self.assertTrue(response == 200)
        self.assertTrue(response == 403)
    
    

if __name__ == '__main__':
    unittest.main()