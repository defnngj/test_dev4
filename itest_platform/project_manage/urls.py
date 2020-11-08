from django.urls import path
from project_manage.views import manage_views


urlpatterns = [
    # 项目管理
    path('', manage_views.manage),
    path('add/', manage_views.project_add),

]


