from pathlib import Path
import json
PATH = '/home/pi/Desktop/ServerFiles/config.txt'
class Config:
    # def __init__(self):

    def file_exists(self):
        config =Path(PATH)
        return config.is_file()

    def make_config(self,str):
        with open(PATH,'w+') as outputfile:
            json.dump(str,outputfile)
    
    def read_config(self,str):
        if self.file_exists():
            with open(PATH) as outputfile:
                return json.loads(outputfile)
        return {}
                

