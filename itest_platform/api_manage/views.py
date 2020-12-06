import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from project_manage.models import Project, Module
from case_manage.models import TestCase
from django.forms.models import model_to_dict


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










