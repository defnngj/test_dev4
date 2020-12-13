from django.shortcuts import render
from task_manage.models import Task


def task_list(request):
    """
    返回task 列表
    :param request:
    :return:
    """
    task = Task.objects.all()
    return render(request, "task.html", {"tasks": task})


def task_add(request):
    """
    task添加页面
    :param request:
    :return:
    """
    return render(request, "task/add.html")
