from django.urls import path
from case_manage import views


urlpatterns = [
    # 用例管理
    path('', views.case_list),
    path('add/', views.case_add),
    path('edit/<int:cid>/', views.case_edit),
    path('delete/<int:cid>/', views.case_add),

]
