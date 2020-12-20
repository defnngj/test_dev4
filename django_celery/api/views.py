from django.shortcuts import render
from django.http import JsonResponse
from api.tasks import add, test_interface


# Create your views here.
def test_task(request):
    #add.delay(2, 2)
    test_interface.delay()
    return JsonResponse({'msg':'interface test task running!'})