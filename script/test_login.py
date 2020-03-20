# 邮箱等哭测试
import time
import unittest

import json
import logging

from parameterized import parameterized

import config
import utils
from utils import DriverUtil

from page.qq_email_login_page import EmailLoginPage


def build_login_data()->list:
    """
    处理json文件参数化
    :return: list格式
    """
    # 初始化一个空列表
    login_data_list = list()
    with open(config.BASE_DIR + '/data/login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = data.get('test_login')
        for item in data_list:
            # 列表添加获取的每一条数据
            login_data_list.append((item.get('username'),
                                    item.get('password'),
                                    item.get('expect')))

        return login_data_list


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器驱动对象
        cls.email_login_page = EmailLoginPage()  # 获取登陆页驱动对象

        cls.driver.switch_to.frame("login_frame")
        cls.email_login_page.account_password_login()  # 点击使用账号密码登陆

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()  # 退出浏览器


    def tearDown(self):
        time.sleep(3)

    @parameterized.expand(build_login_data())
    def test_login(self, username, pwd, expect, ):
        logging.info('username={} pwd={}  expect={}'.format(username, pwd, expect))

        self.email_login_page.input_username(username)  # 输入用户名

        self.email_login_page.input_password(pwd)  # 输入密码

        self.email_login_page.click_login_btn()  # 点击登陆

        # 设置睡眠,等待页面标题的加载
        time.sleep(2)
        # 获取页面标题
        title = self.driver.title

        # 断言判断测试结果
        self.assertIn(expect, title)




