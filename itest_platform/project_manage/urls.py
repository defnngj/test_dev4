from django.urls import path
from project_manage.views import project_views
from project_manage.views import module_views


urlpatterns = [
    # 项目管理
    path('', project_views.manage),
    path('project_add/', project_views.project_add),
    path('project_edit/<int:pid>/', project_views.project_edit),
    path('project_delete/<int:pid>/', project_views.project_delete),

    # 模块管理
    path('module/', module_views.manage),
    path('module_add/', module_views.module_add),
    path('module_edit/<int:mid>/', module_views.module_edit),
    # path('module_delete/<int:mid>/', module_views.project_delete),
]


