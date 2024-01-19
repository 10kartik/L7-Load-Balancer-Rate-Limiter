# Unit test for round robin load balancing, run this test, three server.py servers on ports 5000, 5001, 5002
# and load_balancer.py on port 8000
# Make sure all the servers are running before running this test

import unittest
import requests
import time

class TestRoundRobin(unittest.TestCase):
    responseText = ['5000', '5001', '5002']
    itr = 0
    def test_round_robin(self):
        start_time = time.time()
        while time.time() < start_time + 60:
            response = requests.get('http://127.0.0.1:8000')
            self.assertEqual(response.status_code, 200)
            self.assertIn(response.text, 'Redirected to Flask App running on port ' + self.responseText[self.itr])
            print('Request Served by Server Running on Port {}'.format(self.responseText[self.itr]))
            self.itr += 1
            self.itr %= 3
            time.sleep(5)


if __name__ == '__main__':
    unittest.main()
