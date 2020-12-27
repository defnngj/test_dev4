from django.http import JsonResponse
from api.tasks import running_task
from api.test_case.test_interface import RunConfig


def test_task(request, tid):
    #add.delay(2, 2)
    """
    1. 根据任务的ID 查询所有的用例
    2. 循环执行这些用例
    3. 在执行的时候要把每一次用的结果保存下来。 单独的表保存
    4. 手动的统计 执行结果，执行信息。
    单元测试框架？？ 单元测试框架 + ddt
    """
    running_task.delay(tid)
    return JsonResponse({'msg': 'interface test task running!'})
