from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_manage.models import Project, Module


@login_required  # 控制用户在未登录的情况下不能进入
def manage(request):
    """
    管理页面
    """
    # username = request.COOKIES.get('user', '')
    projects = Project.objects.all()

    username = request.session.get('user', '')
    return render(request, "manage2.html", {"user": username, "projects": projects})


@login_required
def project_add(request):
    """
    项目添加页面
    """
    username = request.session.get('user', '')
    return render(request, "project/add.html")


# 重构
