import unittest
import requests
import xmlrunner
from parameterized import parameterized


class RunConfig:
    task = None  # 1


def test_data():
    print("任务有的id-->", RunConfig.task)
    """
    根据task id 到数据库里面，查询该任务下面的所有用例，组装成一个例表
    """
    data = [
        ("case1", "http://httpbin.org/get", 'get', {"key": "value"}),
        ("case2", "http://httpbin.org/post", 'post', {"key": "value"}),
    ]
    return data


class InterfaceTest(unittest.TestCase):

    @parameterized.expand(test_data)
    def test_case(self, _, url, method, body):
        if method == "get":
            r = requests.get(url, params=body)
            self.assertEqual(r.status_code, 200)
        if method == "post":
            r = requests.post(url, data=body)
            self.assertEqual(r.status_code, 200)
        else:
            pass


if __name__ == '__main__':
    with open('../reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)

