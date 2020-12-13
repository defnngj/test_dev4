from django.db import models


class Task(models.Model):
    """
    测试任务表
    """
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    status = models.IntegerField("状态", default=0)  # 0未执行、1执行中、2.执行完成、3.排队中
    # cases = models.TextField("关联用例", default="[1,2,3,4,5,6]")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name


class TaskCase(models.Model):
    """
    模块表
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    case = models.IntegerField("用例")
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)













