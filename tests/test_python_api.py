import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from PythonDemo_API import app

class TestApp(unittest.TestCase):
    def test_home_route(self):
        tester = app.test_client(self)
        response = tester.get('/gethomes')
        #print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_home_route(self):
        tester = app.test_client(self)
        response = tester.get('/gethomeAddresses')
        print(response.data)
        self.assertEqual(response.status_code, 200) 
if __name__ == '__main__':
    unittest.main()
