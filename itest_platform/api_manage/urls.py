from django.urls import path
from api_manage import views


urlpatterns = [
    # 用例管理
    path('debug/', views.debug),

]
