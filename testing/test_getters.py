import unittest
import os
import sys
import socket
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../model")
from device_info_handler import DeviceInfoHandler
info = DeviceInfoHandler()

class TestGetters(unittest.TestCase):        

    def is_hex(self,s):
        hex_digits = set("0123456789abcdef")
        for char in s:
            if not (char in hex_digits):
                return False
        return True

    def is_valid_ipv4_address(self,address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:  # not a valid address
            return False
        return True

    def is_valid_ipv6_address(self,address):
        try:
            socket.inet_pton(socket.AF_INET6, address)
        except socket.error:  # not a valid address
            return False
        return True

    def test_get_MAC(self):
        self.assertTrue(self.is_hex(info.get_MAC_address()))
    
    def test_get_IP(self):
        IP = info.get_IP_address()
        self.assertTrue(self.is_valid_ipv4_address(IP) or self.is_valid_ipv6_address(IP))

if __name__ == '__main__':
    unittest.main()
        

