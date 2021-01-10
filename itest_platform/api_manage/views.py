import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from project_manage.models import Project, Module
from case_manage.models import TestCase
from django.forms.models import model_to_dict
from task_manage.models import Task, TaskCase
from api_manage.tasks import test_interface
from case_manage.models import TestCase


def debug(request):
    if request.method == "GET":
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": ""})

    req_url = request.POST.get("req_url", "")
    req_method = request.POST.get("req_method", "")
    req_type = request.POST.get("req_type", "")
    req_par = request.POST.get("req_par", "")

    req_par_data = json.loads(req_par)

    result = "没有结果"
    if req_method == "GET":
        r = requests.get(req_url, params=req_par_data)
        result = r.text

    if req_method == "POST":
        if req_type == "data":
            r = requests.post(req_url, data=req_par_data)
            result = r.text
        if req_type == "json":
            r = requests.post(req_url, json=req_par_data)
            result = r.text

    return JsonResponse({"code": 200, "msg": "success", "data": result})


def assert_result(request):
    """
    断言接口返回的结果
    """
    if request.method == "GET":
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": ""})

    result = request.POST.get("assert_result", "")
    text = request.POST.get("assert_text", "")

    if text in result:
        return JsonResponse({"code": 200, "msg": "assert success", "data": ""})
    else:
        return JsonResponse({"code": 10102, "msg": "assert fail", "data": ""})


def select_data(request):
    """
    获取项目/模块的列表，用于select二级菜单的渲染
    """
    if request.method == "POST":
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": ""})

    data_list = []
    project = Project.objects.all()
    for p in project:
        project_dict = {
            "id": p.id,
            "name": p.name,
            "moduleList": []
        }
        # module = Module.objects.filter(project=p)   # 通过对象查询
        module = Module.objects.filter(project_id=p.id)  # 通过对象的id查询
        for m in module:
            module_dict = {
                "id": m.id,
                "name": m.name
            }
            project_dict["moduleList"].append(module_dict)

        data_list.append(project_dict)

    return JsonResponse({"code": 200, "msg": "assert success", "data": data_list})


def add_case(request):
    """
    保存测试用例
    """
    if request.method == "POST":
        case_id = request.POST.get("case_id", "")
        req_url = request.POST.get("req_url", "")
        req_method = request.POST.get("req_method", "")
        req_type = request.POST.get("req_type", "")
        req_par = request.POST.get("req_par", "")
        resp_result = request.POST.get("resp_result", "")
        resp_assert = request.POST.get("resp_assert", "")
        case_module = request.POST.get("case_module", "")
        case_name = request.POST.get("case_name", "")
        print("case_id", case_id)
        if (req_url == "" or req_method == "" or
                resp_result == "" or resp_assert == "" or
                case_module == "" or case_name == ""):
            return JsonResponse({"code": 10102, "msg": "参数错误", "data": ""})

        if req_method == "GET":
            method = 1
        elif req_method == "POST":
            method = 2
        else:
            return JsonResponse({"code": 10103, "msg": "请求方法不支持", "data": ""})

        if req_type == "data":
            type_ = 1
        elif req_type == "post":
            type_ = 2
        else:
            return JsonResponse({"code": 10103, "msg": "请求参数类型不支持", "data": ""})

        if case_id == "":
            # 创建用例
            TestCase.objects.create(
                name=case_name,
                url=req_url,
                method=method,
                request_type=type_,
                request_body=req_par,
                response=resp_result,
                response_assert=resp_assert,
                module_id=case_module,
            )
        else:
            # 保存用例
            print("method", method, type(method))
            case = TestCase.objects.get(id=int(case_id))
            case.name = case_name
            case.url = req_url
            case.method = method
            case.request_type = type_
            case.request_body = req_par
            case.response = resp_result
            case.response_assert = resp_assert
            case.module_id = case_module
            case.save()

        return JsonResponse({"code": 200, "msg": "add success", "data": []})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": ""})


def get_case_info(request, cid):
    """
    获取用例的信息
    """
    if request.method == "GET":
        try:
            case = TestCase.objects.get(id=cid)
        except TestCase.DoesNotExist:
            return JsonResponse({"code": 10102, "msg": "用例信息不存在", "data": []})

        try:
            module = Module.objects.get(id=case.module_id)
        except Module.DoesNotExist:
            return JsonResponse({"code": 10103, "msg": "模块信息不存在", "data": []})

        case_dict = model_to_dict(case)
        case_dict["project"] = module.project_id
        return JsonResponse({"code": 200, "msg": "add success", "data": case_dict})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": ""})


def get_case_tree(request, tid):
    """
    返回项目模块用例的一个树
    """
    if request.method == "GET":
        if tid != 0:
            cases_list = []
            cases = TaskCase.objects.filter(task_id=tid)
            for c in cases:
                cases_list.append(c.case)

        data_list = []
        projects = Project.objects.all()
        for p in projects:
            project_dict = {
                "id": p.id,
                "name": p.name,
                "children": []
            }
            modules = Module.objects.filter(project=p)
            for m in modules:
                module_dict = {
                    "id": m.id,
                    "name": m.name,
                    "children": []
                }
                if tid == 0:
                    cases = TestCase.objects.filter(module=m)
                    for c in cases:
                        case_dict = {
                            "id": c.id,
                            "name": c.name,
                            "checked": False
                        }
                        module_dict["children"].append(case_dict)
                else:
                    cases = TestCase.objects.filter(module=m)
                    for c in cases:
                        if c.id in cases_list:
                            case_dict = {
                                "id": c.id,
                                "name": c.name,
                                "checked": True
                            }
                        else:
                            case_dict = {
                                "id": c.id,
                                "name": c.name,
                                "checked": False
                            }
                        module_dict["children"].append(case_dict)

                project_dict["children"].append(module_dict)
            data_list.append(project_dict)
        return JsonResponse({"code": 10200, "msg": "success", "data": data_list})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": ""})


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
            return JsonResponse({"code": 101001, "msg": "task name is null", "data": []})

        cases_list = json.loads(task_cases)
        if cases_list is []:
            return JsonResponse({"code": 101001, "msg": "select case is null", "data": []})
        print("cccc", task_cases, type(cases_list))

        task = Task.objects.create(name=task_name, describe=task_desc)
        for case in cases_list:
            TaskCase.objects.create(task_id=task.id, case=case)

        return JsonResponse({"code": 10200, "msg": "success", "data": []})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": ""})


def get_task(request, tid):
    """
    获取任务
    """
    if request.method == "GET":
        if tid == "":
            return JsonResponse({"code": 101001, "msg": "task id is null", "data": []})

        try:
            task = Task.objects.get(id=tid)
        except Task.DoesNotExist:
            return JsonResponse({"code": 101002, "msg": "task id error", "data": []})

        task_dict = model_to_dict(task)

        return JsonResponse({"code": 10200, "msg": "success", "data": task_dict})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": ""})


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
            return JsonResponse({"code": 101001, "msg": "task name is null", "data": []})

        cases_list = json.loads(task_cases)
        if cases_list is []:
            return JsonResponse({"code": 101001, "msg": "select case is null", "data": []})
        print("cccc", task_cases, type(cases_list))

        task = Task.objects.get(id=tid)
        task.name = task_name
        task.describe = task_desc
        task.save()

        taskcase = TaskCase.objects.filter(task_id=task.id)
        taskcase.delete()

        for case in cases_list:
            TaskCase.objects.create(task_id=task.id, case=case)

        return JsonResponse({"code": 10200, "msg": "success", "data": []})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": ""})


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
        return JsonResponse({"code": 10200, "msg": "interface test task running!", "data": []})
    else:
        return JsonResponse({"code": 10101, "msg": "请求方法错误", "data": ""})



