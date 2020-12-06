from django.urls import path
from api_manage import views


urlpatterns = [
    # 用例管理
    path('debug/', views.debug),
    path('assert/', views.assert_result),
    path('select_data/', views.select_data),
    path('add_case/', views.add_case),
    path('get_case_info/<int:cid>/', views.get_case_info),

]
