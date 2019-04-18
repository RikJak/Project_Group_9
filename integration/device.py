import uuid
class Device:
    def get_MAC_address(self):
        # mac_address = (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
        # for elements in range(0,2*6,2)][::-1]))
        # return mac_address
        return uuid.getnode()