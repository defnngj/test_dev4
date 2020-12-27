import os
from time import sleep
from celery import shared_task
import requests
import unittest
import xmlrunner
from api.test_case.test_interface import RunConfig

API_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEST_CASE = os.path.join(API_DIR, "api", "test_case")
TEST_REPORT = os.path.join(API_DIR, "api", "reports")

print(TEST_CASE)
print(TEST_REPORT)

# @shared_task
# def add(x, y):
#     sleep(10)
#     return x + y
#
#
# @shared_task
# def mul(x, y):
#     return x * y
#
#
# @shared_task
# def xsum(numbers):
#     return sum(numbers)
#
# @shared_task
# def test():
#     sleep(10)


@shared_task
def running_task(taskID):
    RunConfig.task = taskID
    print("task id-->", RunConfig.task)
    suit = unittest.defaultTestLoader.discover(TEST_CASE)
    report = os.path.join(TEST_REPORT, "002.xml")
    print("--->", report)
    with open(report, 'wb') as output:
        xmlrunner.XMLTestRunner(output=output).run(suit)

    # 把 xml 报告里面的内容写 测试结果表里面

    # r = requests.get('https://api.github.com/events')
    # assert r.status_code == 200


#
# suit = unittest.defaultTestLoader.discover(TEST_CASE)
# with open(TEST_REPORT + '/001.xml', 'wb') as output:
#     xmlrunner.XMLTestRunner(output=output).run(suit)
# print(suit)












