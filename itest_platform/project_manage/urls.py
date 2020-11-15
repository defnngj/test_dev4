from django.urls import path
from project_manage.views import manage_views


urlpatterns = [
    # 项目管理
    path('', manage_views.manage),
    path('project_add/', manage_views.project_add),
    path('project_edit/<int:pid>/', manage_views.project_edit),
    path('project_delete/<int:pid>/', manage_views.project_delete),

]


