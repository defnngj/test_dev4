# test_dev4
测试开发项目


## itest_platform

__安装__

```shell script
pip install -r requirements.txt
```

__运行方式__

1.启动 redis 

```shell script
> redis-server
```

2.启动 celery （进入`itest_platform` 项目目录运行）
```shell script
> celery -A itest_platform worker --loglevel=info
```

3.启动django

```shell script
> python .\manage.py runserver
```
