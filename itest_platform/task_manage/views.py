from django.shortcuts import render
from task_manage.models import Task
from task_manage.models import TestResult
from django.http import JsonResponse


def task_list(request):
    """
    返回task 列表
    """
    task = Task.objects.all()
    return render(request, "task.html", {"tasks": task})


def task_add(request):
    """
    task添加页面
    """
    return render(request, "task/add.html")


def task_edit(request, tid):
    """
    task添加页面
    """
    return render(request, "task/edit.html")


def task_results(request, tid):
    """
    task执行结果
    """
    test_results = TestResult.objects.filter(task_id=tid).order_by("-create_time")
    return render(request, "task/results.html", {"results": test_results})


def show_result(request, rid):
    """
    查看报告的详情
    """
    result = TestResult.objects.get(id=rid)
    print(result.result)
    return render(request, "3_1610265980.xml")


def task_delete(request, tid):
    """
    task添加页面
    """
    pass


def task_running(request):
    """
    task添加页面
    """
    pass