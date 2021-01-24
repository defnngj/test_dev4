from django.test import TestCase
from django.contrib.auth.models import User


class LoginPageTest(TestCase):
    """
    登录页面的测试
    """

    def test_login_page(self):
        # Issue a GET request.
        response = self.client.get('/index/')
        print("返回结果", response.status_code)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIn(b"itest platform", response.content)


class LoginActionTest(TestCase):
    """
    登录功能的测试
    """

    def setUp(self):
        User.objects.create_user(username="admin", email="admin@126.com", password="a123")

    def test_login_null(self):
        """
        测试登录账号为空
        """
        response = self.client.post('/index/', {'username': '', 'password': ''})
        print("返回结果", response.status_code)
        # print("返回结果", response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The username or password is empty', response.content)

    def test_login_fail(self):
        """
        测试登录失败
        """
        response = self.client.post('/index/', {'username': 'abc', 'password': '123'})
        print("返回结果", response.status_code)
        # print("返回结果", response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Wrong user name or password!', response.content)

    def test_login_successful(self):
        """
        测试登录成功
        """
        response = self.client.post('/index/', {'username': 'admin', 'password': 'a123'})
        print("返回结果", response.status_code)
        self.assertEqual(response.status_code, 302)



















