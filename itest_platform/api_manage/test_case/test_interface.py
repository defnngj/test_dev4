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
    def test_case(self, _, url, method, request_type, body, response_assert):
        msg = """接口信息：url:{u}, 
                 method:{m}, 
                 request_type:{rt}, 
                 body:{b},
                 response_assert:{ra}""".format(u=url, m=method, rt=request_type, b=body, ra=response_assert)
        if method == 1:  # get
            r = requests.get(url, params=body)
            self.assertEqual(r.status_code, 200)
            self.assertIn(response_assert, r.text)
        if method == 2:  # post
            if request_type == 1:  # from-data
                r = requests.post(url, data=body)
                self.assertEqual(r.status_code, 200)
                self.assertIn(response_assert, r.text)
            if request_type == 2:  # json
                r = requests.post(url, json=body)
                self.assertEqual(r.status_code, 200)
                self.assertIn(response_assert, r.text)
            else:
                print(msg)
        else:
            print(msg)


if __name__ == '__main__':
    with open('../reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)

