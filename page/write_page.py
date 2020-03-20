"""qq邮箱写信页面"""

from base.base import Base
from page.UIElements import UIElements


class WritePage(Base):
    def __init__(self):
        super().__init__()

    def input_recipient_box(self, user_email):
        """输入收件人账号"""
        self.send_element(UIElements.Recipient_input_box, user_email)

    def input_subject_box(self, theme):
        """输入内容主题"""
        self.send_element(UIElements.Subject_input_box, theme)

    def input_text(self, text):
        """输入正文内容"""
        self.send_element(UIElements.text_input, text)

    def click_send_btn(self):
        """点击发送按钮"""
        self.click_element(UIElements.send_btn)

    def click_return_homepage(self):
        """点击返回邮箱首页"""
        self.click_element(UIElements.Return_homepage)

    def get_text(self):
        """获取返回邮箱首页文字"""
        msg = self.driver.find_element_by_id('sendinfomsg').text

        return msg
