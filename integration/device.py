import uuid
import socket 

class Device:
    def get_MAC_address(self):
        """
        Finds the MAC address of the device
        @output: the MAC address of the device
        """
        return hex(uuid.getnode())

    def get_IP_address(self):
        """
        Finds the IP of the device by connecting to a remote ip and getting the ip from the socket used.
        @output: The IP of the device. 'xxx.xxx.xxx.xxx'
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP