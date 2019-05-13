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
        """
        Validates the user. If the user is valid it will turn any sensors and running streams off.
        It will then start a new video_stream server from the commandline. 
        It has a wait before it returns to make sure that the server is up before the user tries to access it.
        @input: email,api_key,client_IP, device_IP
        @output: {'port':PORT, 'server_ip': server_IP}
        """
        try:
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

                    time.sleep(1)
                except:
                    print("Video stream was not active")

                # subprocess.call(['python3', '/home/Project_Group_9/model/video_stream.py', str(client_ip), str(PORT)])
                # call(f"python3 /home/Project_Group_9/model/video_stream.py {client_ip} {PORT}", shell=True)
                # run("/home/Project_Group_9/model/video_stream.py", client_ip, PORT)
                start_command = f"sudo python3 /home/Project_Group_9/model/video_stream.py {client_ip} {PORT} {server_IP} &"
                os.system(start_command)
                time.sleep(5)
                return json.dumps({'port':PORT, 'server_ip': server_IP})
            return '', 403
        except:
            return '', 500

    def reboot(self,email,api_key):
        """
        Reboots the raspberryPi
        @input: email,api_key
        @output: error
        """
        valid = self.validate.validate_user(email,api_key)
        valid = True # will be removed if real validation is made!
        if (valid):
            os.system('sudo reboot')
            return {'msg': 'Rebooting'}
        return '', 403