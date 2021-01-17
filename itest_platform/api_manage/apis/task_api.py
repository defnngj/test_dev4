import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from app_manage.models import Task, TaskCase
from app_manage.models import TestCase
from api_manage.common import resp
from api_manage.tasks import test_interface


def add_task(request):
    """
    添加任务
    """
    if request.method == "POST":
        task_name = request.POST.get("task_name", "")
        task_desc = request.POST.get("task_desc", "")
        task_cases = request.POST.get("task_cases", "")

        print("dddd", task_cases, type(task_cases))

        if task_name == "":
            return resp(101001, msg="task name is null", data=[])

        cases_list = json.loads(task_cases)
        if cases_list is []:
            return resp(101001, msg="select case is null", data=[])
        print("cccc", task_cases, type(cases_list))

        task = Task.objects.create(name=task_name, describe=task_desc)
        for case in cases_list:
            TaskCase.objects.create(task_id=task.id, case=case)

        return resp(10200, msg="success", data=[])
    else:
        return resp(10101, msg="请求方法错误", data="")


def get_task(request, tid):
    """
    获取任务
    """
    if request.method == "GET":
        if tid == "":
            return resp(101001, msg="task id is null", data=[])

        try:
            task = Task.objects.get(id=tid)
        except Task.DoesNotExist:
            return resp(101002, msg="task id error", data=[])

        task_dict = model_to_dict(task)

        return resp(10200, msg="success", data=task_dict)
    else:
        return resp(10101, msg="请求方法错误", data="")


def edit_task(request, tid):
    """
    编辑任务保存
    """
    if request.method == "POST":
        task_name = request.POST.get("task_name", "")
        task_desc = request.POST.get("task_desc", "")
        task_cases = request.POST.get("task_cases", "")

        print("dddd", task_cases, type(task_cases))

        if task_name == "":
            return resp(101001, msg="task name is null", data=[])

        cases_list = json.loads(task_cases)
        if cases_list is []:
            return resp(101001, msg="select case is null", data=[])
        print("cccc", task_cases, type(cases_list))

        task = Task.objects.get(id=tid)
        task.name = task_name
        task.describe = task_desc
        task.save()

        taskcase = TaskCase.objects.filter(task_id=task.id)
        taskcase.delete()

        for case in cases_list:
            TaskCase.objects.create(task_id=task.id, case=case)

        return resp(10200, msg="success", data=[])
    else:
        return resp(10101, msg="请求方法错误", data="")


def test_data(tid):
    print("任务有的id-->", tid)
    tcase = TaskCase.objects.filter(task_id=tid)
    data = []
    for c in tcase:
        case = TestCase.objects.get(id=c.case)
        case_tup = (
            case.name,
            case.url,
            case.method,
            case.request_type,
            case.request_body,
            case.response_assert,
        )
        data.append(case_tup)

    """
    根据task id 到数据库里面，查询该任务下面的所有用例，组装成一个例表
    """
    # data = [
    #     ("case1", "http://httpbin.org/get", 'get', {"key": "value"}),
    #     ("case2", "http://httpbin.org/post", 'post', {"key": "value"}),
    # ]
    print("data--->", data)
    return data


def running_task(request, tid):
    """
    运行测试任务
    1. 根据任务的ID 查询所有的用例
    2. 循环执行这些用例
    3. 在执行的时候要把每一次用的结果保存下来。 单独的表保存
    4. 手动的统计 执行结果，执行信息。
    单元测试框架？？ 单元测试框架 + ddt
    """
    if request.method == "GET":
        data = test_data(tid)
        test_interface.delay(tid, data)
        task = Task.objects.get(id=tid)
        task.status = 1
        task.save()
        return resp(10200, msg="interface test task running!", data=[])
    else:
        return resp(10101, msg="请求方法错误", data="")

