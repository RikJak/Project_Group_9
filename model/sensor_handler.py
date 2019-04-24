import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")
from validate import Validate
import json
PORT = 6000
class SensorHandler():
    def __init__(self):
        self.validate = Validate()

    def start_sensor(self,email,api_key,client_ip,server_IP):
        valid = self.validate.validate_user(email,api_key)
        if (valid):
            start_command = f"sudo python3 /home/Project_Group_9/model/video_stream.py {client_ip} {PORT} {server_IP} &"
            os.system(start_command)
            return json.dumps({'port':PORT, 'server_ip': server_IP})
        return '', 403
