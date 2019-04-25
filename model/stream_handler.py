import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")

import time
from validate import Validate
import json
import requests
from subprocess import call
PORT = 8000
class StreamHandler:
    def __init__(self):
        self.validate= Validate()
        

    def set_up_stream(self,email,api_key,client_ip,server_IP):
        valid = self.validate.validate_user(email,api_key)
        if (valid):
            try:
                requests.post(f"http://{server_IP}:6000/sensor_off")
            except:
                print("Sensor was not active")
            try:
                content = {'email':email,'api_key':api_key}
                content = json.dumps(content)
                headers = {"Content-Type":"application/json"}
                requests.post(f"http://{server_IP}:8000/shutdown_stream", data = content,headers = headers,verify=False)
            except:
                print("Video stream was not active")

            # subprocess.call(['python3', '/home/Project_Group_9/model/video_stream.py', str(client_ip), str(PORT)])
            # call(f"python3 /home/Project_Group_9/model/video_stream.py {client_ip} {PORT}", shell=True)
            # run("/home/Project_Group_9/model/video_stream.py", client_ip, PORT)
            start_command = f"sudo python3 /home/Project_Group_9/model/video_stream.py {client_ip} {PORT} {server_IP} &"
            os.system(start_command)
            time.sleep(3)
            return json.dumps({'port':PORT, 'server_ip': server_IP})
        return '', 403

    def reboot(self,email,api_key):
        valid = self.validate.validate_user(email,api_key)
        valid = True # will be removed if real validation is made!
        if (valid):
            os.system('sudo reboot')
            return {'msg': 'Rebooting'}
        return '', 403