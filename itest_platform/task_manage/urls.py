from django.urls import path
from task_manage import views


urlpatterns = [
    # 任务管理
    path('', views.task_list),
    path('add/', views.task_add),

]


