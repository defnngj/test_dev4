import os
import time
import json
from celery import shared_task
import unittest
import xmlrunner
from api_manage.test_case.config import RunConfig
from xml.dom.minidom import parse
from task_manage.models import TestResult
from task_manage.models import Task

API_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEST_CASE = os.path.join(API_DIR, "api_manage", "test_case")
TEST_REPORT = os.path.join(API_DIR, "static", "reports")
TEST_DATA = os.path.join(TEST_CASE, "test_data.json")


@shared_task
def test_interface(taskID, data):
    # 测试数据赋值给 RunConfig.data
    RunConfig.data = data
    # RunConfig.data.remove(RunConfig.data[0])
    # 定义测试套件
    suit = unittest.defaultTestLoader.discover(TEST_CASE)
    # 定义测试任务报告的名字
    task_report_name = str(taskID) + "_" + str(time.time()).split(".")[0] + ".xml"
    report = os.path.join(TEST_REPORT, task_report_name)
    print("测试报告---->", report)
    # 运行测试套件，生成测试报告
    with open(report, 'wb') as output:
        xmlrunner.XMLTestRunner(output=output).run(suit)

    # 判断测试报告是否生成, 如果生成读取报告的内容
    if os.path.exists(report) is True:
        # 打开xml文档
        dom = parse(report)
        # 得到文档元素对象
        root = dom.documentElement
        # 获取(一组)标签  测试套件
        testsuite = root.getElementsByTagName('testsuite')
        errors = testsuite[0].getAttribute("errors")
        failures = testsuite[0].getAttribute("failures")
        name = testsuite[0].getAttribute("name")
        skipped = testsuite[0].getAttribute("skipped")
        tests = testsuite[0].getAttribute("tests")
        run_time = testsuite[0].getAttribute("time")
        print(errors)
        print(failures)
        print(name)
        print(skipped)
        print(tests)
        print(run_time)
        save_report = report.split("itest_platform")[1].replace('\\static', '/static')
        TestResult.objects.create(name=name, task_id=taskID,
                                  error=errors, failure=failures,
                                  skipped=skipped, tests=tests, run_time=run_time,
                                  result=save_report)
        task = Task.objects.get(id=taskID)
        task.status = 2
        task.save()











