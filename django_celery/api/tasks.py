from time import sleep
from celery import shared_task
import requests


@shared_task
def add(x, y):
    sleep(10)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def test():
    sleep(10)

@shared_task
def test_interface():
    r = requests.get('https://api.github.com/events')
    assert r.status_code == 200
    print(r.json())
