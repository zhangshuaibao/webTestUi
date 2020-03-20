"""qq邮箱登陆页面"""
from base.base import Base
from page.UIElements import UIElements
import json
import config
import logging

class EmailLoginPage(Base):

    def __init__(self):
        super().__init__()

    def account_password_login(self):
        """点击账号密码登陆"""
        self.click_element(UIElements.Account_password_login_btn)

    def input_username(self, username):
        """输入用户名"""
        self.send_element(UIElements.input_user_name, username)

    def input_password(self, pwd):
        """输入密码"""
        self.send_element(UIElements.input_password, pwd)

    def click_login_btn(self):
        """点击登陆按钮"""
        self.click_element(UIElements.login_button)
