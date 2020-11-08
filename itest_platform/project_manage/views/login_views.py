from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from project_manage.models import Project, Module


# Create your views here.
def hello(request):
    if request.method == "GET":
        print("get 请求")
        name = request.GET.get("name", "")
        print("--->", name)
        return render(request, "hello.html", {"n": name})


def index(request):
    """
    实现登录
    """
    # 返回登录页面
    if request.method == "GET":
        return render(request, "login.html")

    # 处理登录的数据
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        print("__>", username, password)
        if username == "" or password == "":
            return render(request, "login.html", {"error": "The username or password is empty"})

        user = auth.authenticate(username=username, password=password)
        print("==>", user)
        if user is not None:
            auth.login(request, user)  # 到数据库写 session_key
            response = HttpResponseRedirect("/manage/")
            # response.set_cookie("user", username, 3600)
            request.session['user'] = username
            return response
        else:
            return render(request, "login.html", {"error": "Wrong user name or password!"})


@login_required
def logout(request):
    """
    退出系统
    """
    auth.logout(request)  # 到数据库删除 session_key
    return HttpResponseRedirect("/index/")
