from django.urls import path
from case_manage import views


urlpatterns = [
    # 用例管理
    path('', views.case_list),

]
