from django.test import TestCase
from django.contrib.auth.models import User
from app_manage.models import Project


class ProjectTest(TestCase):
    """
    项目管理的测试
    """
    def setUp(self):
        Project.objects.create(name="project qq", describe="desc", status=False)
        User.objects.create_user(username="admin", email="admin@126.com", password="a123")
        self.client.post('/index/', {'username': 'admin', 'password': 'a123'})

    def test_login_page(self):
        # Issue a GET request.
        response = self.client.get('/project/')
        print("返回结果", response.status_code)
        print('项目页面', response.content)

        # # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/project.html')
        self.assertIn(b"project qq", response.content)












