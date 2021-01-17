import unittest
from django.test import TestCase
from app_manage.models import Project


# django.test 继承 unittest
# django 运行测试的时候不会真的把数据写到表里面。好处：重复的执行
class ProjectTest(TestCase):
    # django 的模型测试

    def setUp(self) -> None:
        Project.objects.create(name="项目qq", describe="描述", status=False)

    def test_create(self):
        Project.objects.create(name="美团外卖", describe="1111", status=True)
        p = Project.objects.get(name='美团外卖')
        self.assertEqual(p.name, "美团外卖")
        self.assertEqual(p.describe, "1111")
        self.assertEqual(p.status, True)

    def test_delete(self):
        p = Project.objects.get(name='项目qq')
        p.delete()
        ret = Project.objects.filter(name='项目qq')
        self.assertEqual(len(ret), 0)

    def test_update(self):
        p = Project.objects.get(name='项目qq')
        p.name = "项目PP"
        p.describe = "2222"
        p.status = True
        p.save()
        ret = Project.objects.get(name='项目PP')
        self.assertEqual(ret.name, "项目PP")
        self.assertEqual(ret.describe, "2222")
        self.assertEqual(ret.status, True)

    def test_query(self):
        Project.objects.create(name="项目aa", describe="333", status=False)

        p = Project.objects.get(name='项目qq')
        self.assertEqual(p.name, "项目qq")
        self.assertEqual(p.describe, "描述")
        self.assertEqual(p.status, False)

        ps = Project.objects.filter(name__contains='项目')
        self.assertEqual(len(ps), 2)







