from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.models import Module
from app_manage.forms import ModuleForm


@login_required
def module(request):
    """
    模块管理页面
    """
    modules = Module.objects.all()
    username = request.session.get('user', '')
    return render(request, "module/module.html", {"user": username, "modules": modules})


@login_required
def module_add(request):
    """
    添加模块页面
    """
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            Module.objects.create(name=name, describe=describe, project=project)
            return HttpResponseRedirect('/manage/module/')
    else:
        form = ModuleForm()
        username = request.session.get('user', '')
        return render(request, "module/add.html", {"user": username, "form": form})


@login_required
def module_edit(request, mid):
    """
    模块更新
    """
    username = request.session.get('user', '')

    if request.method == "POST":
        # 表单已经修改了数据，提高之后更新表里面的数据
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = Module.objects.get(id=mid)
            module.project = form.cleaned_data['project']
            module.name = form.cleaned_data['name']
            module.describe = form.cleaned_data['describe']
            module.save()
            return HttpResponseRedirect('/manage/module/')
    else:
        # 打开表单页面，把旧的要编辑的数据写到表单里面
        if mid:
            try:
                m = Module.objects.get(id=mid)
                form = ModuleForm(instance=m)
                return render(request, "module/edit.html",
                              {"user": username, "form": form, "mid": mid})
            except Module.DoesNotExist:
                return HttpResponseRedirect('/manage/module/')
