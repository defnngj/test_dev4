from django.urls import path
from app_manage.views import user_view
from app_manage.views import project_view
from app_manage.views import module_view
from app_manage.views import case_view
from app_manage.views import task_view


urlpatterns = [
    path('', user_view.index),
    path('index/', user_view.index),
    path('accounts/login/', user_view.index),
    path('logout/', user_view.logout),

    # 项目管理
    path('project/', project_view.project),
    path('project/add/', project_view.project_add),
    path('project/edit/<int:pid>/', project_view.project_edit),
    path('project/delete/<int:pid>/', project_view.project_delete),

    # 模块管理
    path('module/', module_view.module),
    path('module/add/', module_view.module_add),
    path('module/edit/<int:mid>/', module_view.module_edit),
    # path('module_delete/<int:mid>/', module_views.project_delete),

    # 用例管理
    path('case/', case_view.case_list),
    path('case/add/', case_view.case_add),
    path('case/edit/<int:cid>/', case_view.case_edit),
    path('case/delete/<int:cid>/', case_view.case_delete),

    # 任务管理
    path('task/', task_view.task_list),
    path('task/add/', task_view.task_add),
    path('task/edit/<int:tid>/', task_view.task_edit),
    path('task/delete/<int:tid>/', task_view.task_delete),
    path('task/results/<int:tid>/', task_view.task_results),
    path('task/result/<int:rid>/', task_view.show_result),
    path('task/running/', task_view.task_running),
]




















