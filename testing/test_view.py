import unittest
import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../")

from view.view import View

view = View()
class TestView(unittest.TestCase):

    def test_post_request(self):
        
    
    

if __name__ == '__main__':
    unittest.main()