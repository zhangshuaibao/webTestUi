# 读取邮件/
import time
import unittest
import utils
from page.qq_email_homepage import EmailHomePage
from page.receiving_page import REceivingPage
from utils import DriverUtil


class TestReturn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器驱动对象

        cls.receiving_page = REceivingPage()  # 获取收件页面驱动对象
        cls.email_home_page = EmailHomePage()  # 获取邮箱首页驱动对象

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()  # 退出浏览器

    def setUp(self):
        utils.switch_to_frame('', dr=3)  # 切换至父级frame
        time.sleep(3)

    def tearDown(self):
        time.sleep(3)

    def test_cat(self):
        self.email_home_page.click_inbox_btn()  # 点击收件箱

        utils.switch_to_frame("mainFrame")  # 切换新的frame

        self.receiving_page.click_app_btn()  # 点击具体邮件

        self.assertTrue('1261902892@qq.com', self.receiving_page.assert_text())  # 判断当前页面是否有邮箱
