from django.urls import path
from api_manage.apis import case_api, task_api


urlpatterns = [
    # 用例api
    path('debug/', case_api.debug),
    path('assert/', case_api.assert_result),
    path('select_data/', case_api.select_data),
    path('add_case/', case_api.add_case),
    path('get_case_info/<int:cid>/', case_api.get_case_info),
    path('get_case_tree/<int:tid>/', case_api.get_case_tree),

    # 任务api
    path('add_task/', task_api.add_task),
    path('get_task/<int:tid>/', task_api.get_task),
    path('edit_task/<int:tid>/', task_api.edit_task),

    # 任务执行api
    path('run_task/<int:tid>/', task_api.running_task),
]
