# page 基类
from utils import DriverUtil


class Base(object):
    """page基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def get_element(self, loc):
        """
        单个元素定位(利用拆包获取元组属性值)
        :param loc: 元素对象定位方法类型和属性值
        :return: 元素对象
        """
        return self.driver.find_element(*loc)

    def get_elements(self, loc):
        """
        定位一组元素
        :param loc: (By.ID,id属性值) (By.CLASS_NAME,class属性值) (By.XPATH,xpath属性值)
        :return:元素定位对象列表
        """
        return self.driver.find_elements(*loc)

    def click_element(self, loc):
        """
        点击元素
        :param loc: (By.ID,id属性值) (By.CLASS_NAME,class属性值) (By.XPATH,xpath属性值)
        :return:
        """
        self.get_element(loc).click()

    def send_element(self, loc, text):
        """
        输入文本内容
        :param loc: (By.ID,id属性值) (By.CLASS_NAME,class属性值) (By.XPATH,xpath属性值)
        :param text: 输入文本内容
        :return:
        """
        # 定位元素
        input_text = self.get_element(loc)
        # 清空输入框
        input_text.clear()
        # 输入元素
        input_text.send_keys(text)

    def get_text_information(self, loc):
        """
        获取当前元素的文本信息
        :param loc: (By.ID,id属性值) (By.CLASS_NAME,class属性值) (By.XPATH,xpath属性值)
        :return:
        """
        return self.get_element(loc).text
