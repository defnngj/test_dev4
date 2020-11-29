import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from project_manage.models import Project, Module


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














