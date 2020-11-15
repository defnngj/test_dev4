from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_manage.models import Project, Module
from project_manage.forms import ProjectForm


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
    项目添加
    """
    print("adfasdfas-->", request.method)
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name, describe=describe, status=status)
            return HttpResponseRedirect('/manage/')
    else:
        form = ProjectForm()
        username = request.session.get('user', '')
        return render(request, "project/add.html", {"user": username, "form": form})


@login_required
def project_edit(request, pid):
    """
    项目更新
    """
    username = request.session.get('user', '')
    print("pid", pid)
    if request.method == "POST":
        # 表单已经修改了数据，提高之后更新表里面的数据
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.get(id=pid)
            project.name = form.cleaned_data['name']
            project.describe = form.cleaned_data['describe']
            project.status = form.cleaned_data['status']
            project.save()
            return HttpResponseRedirect('/manage/')
    else:
        # 打开表单页面，把旧的要编辑的数据写到表单里面
        if pid:
            try:
                p = Project.objects.get(id=pid)
                form = ProjectForm(instance=p)
                return render(request, "project/edit.html",
                              {"user": username, "form": form, "pid": pid})
            except Project.DoesNotExist:
                return HttpResponseRedirect('/manage/')


def project_delete(request, pid):
    """
    删除项目
    """
    try:
        p = Project.objects.get(id=pid)
        p.delete()
    except Project.DoesNotExist:
        return HttpResponseRedirect('/manage/')
    else:
        return HttpResponseRedirect('/manage/')










