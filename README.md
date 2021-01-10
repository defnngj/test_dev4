# test_dev4
测试开发项目


## itest_platform

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

项目的重构 
- 在不改变功能的基础上，重新设计项目结构，更容易扩展，维护，后续开发效率更高

项目的部署：
wsgi nginx 部署到主机 
