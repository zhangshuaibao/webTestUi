"""收件箱页面"""

from base.base import Base
from page.UIElements import UIElements
import utils


class REceivingPage(Base):

    def __init__(self):
        super().__init__()

    def click_app_btn(self):
        """点击具体邮件"""
        self.click_element(UIElements.apple_email)

    def assert_text(self):
        """获取页面文本信息"""

        return self.get_text_information(UIElements.user_email)
