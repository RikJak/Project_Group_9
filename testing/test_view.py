import os
import sys
import requests
import json
import unittest
from unittest.mock import patch
from unittest import TestCase


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../")
SERVER_IP_PORT = '130.237.215.167:5000'

class TestView(unittest.TestCase):

    @patch('requests.post')
    def test_post_start_stream(self,mock_post):
        info = {"api_key": "Db-fNOW05Mwe4dcN8AhRdNPRSCtQi8PUInt5Uy3Q", "email": "mhild@kth.se"}
        resp = requests.post("http://130.237.215.167:5000", data=json.dumps(info), headers={'Content-Type': 'application/json'})
        mock_post.assert_called_with("http://130.237.215.167:5000", data=json.dumps(info), headers={'Content-Type': 'application/json'})

    @patch('requests.post')
    def test_post_change_res(self,mock_post):
        info = {"res_x": "1920", "res_y": "1080"}
        resp = requests.post("130.237.215.167:8000/settings", data=json.dumps(info), headers={'Content-Type': 'application/json'})
        mock_post.assert_called_with("130.237.215.167:8000/settings", data=json.dumps(info), headers={'Content-Type': 'application/json'})

if __name__ == '__main__':
    unittest.main()