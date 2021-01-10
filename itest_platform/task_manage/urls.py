from django.urls import path
from task_manage import views


urlpatterns = [
    # 任务管理
    path('', views.task_list),
    path('add/', views.task_add),
    path('edit/<int:tid>/', views.task_edit),
    path('delete/<int:tid>/', views.task_delete),
    path('results/<int:tid>/', views.task_results),
    path('result/<int:rid>/', views.show_result),
    path('running/', views.task_running),
]


