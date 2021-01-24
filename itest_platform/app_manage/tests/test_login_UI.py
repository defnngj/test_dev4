from time import sleep
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from django.contrib.auth.models import User


class LoginTest(StaticLiveServerTestCase):

    def setUp(self):
        User.objects.create_user(username="admin", email="admin@126.com", password="a123")
        self.browser = Chrome()
        self.browser.implicitly_wait(10)

    def test_login_null(self):
        print("url-->",self.live_server_url)
        self.browser.get(self.live_server_url + "/index/")
        self.browser.find_element_by_name("username").send_keys("")
        self.browser.find_element_by_name("password").send_keys("")
        self.browser.find_element_by_id('login-button').click()
        sleep(2)
        text = self.browser.find_element_by_id("hint").text
        self.assertEqual(text, "The username or password is empty")

    def test_login_fail(self):
        print("url-->",self.live_server_url)
        self.browser.get(self.live_server_url + "/index/")
        self.browser.find_element_by_name("username").send_keys("abc")
        self.browser.find_element_by_name("password").send_keys("123")
        self.browser.find_element_by_id('login-button').click()
        sleep(2)
        text = self.browser.find_element_by_id("hint").text
        self.assertEqual(text, "Wrong user name or password!")

    def test_login_success(self):
        print("url-->",self.live_server_url)
        self.browser.get(self.live_server_url + "/index/")
        self.browser.find_element_by_name("username").send_keys("admin")
        self.browser.find_element_by_name("password").send_keys("a123")
        self.browser.find_element_by_id('login-button').click()
        sleep(2)
        url = self.browser.current_url
        user = self.browser.find_element_by_css_selector(".account-user-name").text
        self.assertIn("project", url)
        self.assertEqual(user, "admin")










