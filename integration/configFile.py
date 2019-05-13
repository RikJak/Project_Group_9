from pathlib import Path
import json
PATH = '/home/pi/Desktop/ServerFiles/config.txt'
class Config():
    # def __init__(self):

    def file_exists(self):
        """
        Checks if the config file currently exists
        @output: boolean
        """
        config =Path(PATH)
        return config.is_file()

    def make_config(self,str):
        """
        Creates a config file with the provided data.
        It writes the data to the file using JSON
        """
        with open(PATH,'w+') as outputfile:
            json.dump(str,outputfile)
    
    def get_local_IP(self):
        """
        Gets the local IP that was registered in the config file
        @output: {'local_ip': 'xxx.xxx.xxx.xxx'}/{} if no config file exists
        """
        if self.file_exists():
            with open(PATH) as outputfile:
                return json.load(outputfile)['local_IP']
        return {}

    def get_webserver_IP(self):
        """
        Gets the webserver address that was registered in the config file.
        @output: {'webserver_ip': 'www.xxxxx.xx'}/{} if no config file exists
        """
        if self.file_exists():
            with open(PATH) as outputfile:
                return json.load(outputfile)['webserver_IP']
        return {}
                    
                

