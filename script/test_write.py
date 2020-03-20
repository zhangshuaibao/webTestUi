# 订单提交测试(不能单独执行)
import time
import unittest

from utils import switch_to_frame
from page.qq_email_homepage import EmailHomePage
from page.write_page import WritePage
from utils import DriverUtil


class TestWrite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器驱动对象
        cls.email_home_page = EmailHomePage()  # 获取首页驱动对象
        cls.email_write_page = WritePage()  # 获取写信页面驱动对象

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def setUp(self):
        # self.driver.get(
        #     'https://mail.qq.com/cgi-bin/frame_html?sid=DCDOUEwWdEPTWxBN&r=393a0a38f07e6e685da3d48a88d09023')
        self.email_home_page.clcik_write_a_letter()  # 点击写信按钮
        time.sleep(5)

    def test_input_email_data(self):
        switch_to_frame('mainFrame')

        self.email_write_page.input_recipient_box('820424843@qq.com')  # 输入收件人地址

        self.email_write_page.input_subject_box('哈哈哈啊哈哈哈')  # 输入邮件主题
        switch_to_frame("", dr=3)  # 回到主frame

        switch_to_frame('mainFrame')

        frame_boby = self.driver.find_element_by_xpath('//iframe[@scrolling="auto"]')

        self.driver.switch_to.frame(frame_boby)
        self.email_write_page.input_text('啦啦啦我是一个啊啊啊啊啊啊啊啊')  # 输入邮件正文
        switch_to_frame('', dr=2)  # 回到上一个frame

        self.email_write_page.click_send_btn()  # 点击发送按钮

        self.assertTrue('您的邮件发送成功', self.email_write_page.get_text())  # 断言是否发送成功
    #
