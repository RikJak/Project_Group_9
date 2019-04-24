import unittest
import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../")

from integration.validate import Validate
TEST_USER = 'mhild@kth.se'
TEST_KEY = 'Db-fNOW05Mwe4dcN8AhRdNPRSCtQi8PUInt5Uy3Q'
TEST_INVALID_USER = 'hej@kth.se'
TEST_INVALID_KEY = 'Db-fNOW05Mwe4dcN8AhsdafsljkCtQi8PUInt5Uy3Q'
validate = Validate()
class TestDBConnection(unittest.TestCase):

    def test_validation(self):
        self.assertTrue(validate.validate_user(TEST_USER,TEST_KEY))
        self.assertFalse(validate.validate_user(TEST_INVALID_USER,TEST_KEY))
        self.assertFalse(validate.validate_user(TEST_USER,TEST_INVALID_KEY))
        self.assertFalse(validate.validate_user(TEST_INVALID_USER,TEST_INVALID_KEY))
    
if __name__ == '__main__':
    unittest.main()