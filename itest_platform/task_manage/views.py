from django.shortcuts import render
from task_manage.models import Task


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