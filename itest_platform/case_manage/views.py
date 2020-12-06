from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_manage.models import Project, Module
from project_manage.forms import ModuleForm
from case_manage.models import TestCase


@login_required
def case_list(request):
    """
    用例管理
    """
    cases = TestCase.objects.all()
    return render(request, "case.html", {
        "cases": cases
    })


@login_required
def case_add(request):
    """
    用例添加页面
    """
    return render(request, "case/postman.html")


@login_required
def case_edit(request, cid):
    """
    用例编辑页面
    """
    return render(request, "case/edit.html")


@login_required
def case_delete(request, cid):
    """
    用例编辑页面
    """
    TestCase.objects.get(id=cid).delete()
    return HttpResponseRedirect("/case/")






















