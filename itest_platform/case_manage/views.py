from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_manage.models import Project, Module
from project_manage.forms import ModuleForm


@login_required
def case_list(request):
    """
    用例管理
    """
    return render(request, "postman.html")
