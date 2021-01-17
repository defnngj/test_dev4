from django.http import JsonResponse


def resp(code=None, msg=None, data=None):
    """
    定义返回接口格式
    """
    if code is None:
        code = 10200
    if msg is None:
        msg = "success"
    if data is None:
        data = []
    return JsonResponse({"code":code, "msg": msg, "data": data})
