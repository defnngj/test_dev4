import os
import unittest
import requests
import xmlrunner
from parameterized import parameterized
from api_manage.test_case.config import RunConfig
from ddt import ddt,file_data, unpack
CASE_DIR = os.path.dirname(os.path.abspath(__file__))

# TEST_DATA = os.path.join(CASE_DIR, "test_data.json")


class InterfaceTest(unittest.TestCase):

    @parameterized.expand(RunConfig.data)
    def test_case(self, _, url, method, body):
        print(url)
        if method == 1:
            r = requests.get(url, params=body)
            self.assertEqual(r.status_code, 200)
        if method == 2:
            r = requests.post(url, data=body)
            self.assertEqual(r.status_code, 200)
        else:
            pass


if __name__ == '__main__':
    with open('../reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)

