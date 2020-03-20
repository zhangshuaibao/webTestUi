"""qq邮箱首页"""
from base.base import Base
from page.UIElements import UIElements


class EmailHomePage(Base):
    def __init__(self):
        super().__init__()

    def clcik_write_a_letter(self):
        """点击首页写信按钮"""
        self.click_element(UIElements.write_a_letter_btn)

    def click_inbox_btn(self):
        """点击首页收件箱按钮"""
        self.click_element(UIElements.inbox_btn)
