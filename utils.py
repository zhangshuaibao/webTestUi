# 公共方法类
from selenium import webdriver


def switch_to_new_window():
    """切换新窗口方法"""
    driver = DriverUtil.get_driver()
    driver.switch_to.window(driver.window_handles[-1])


def exist_text(text):
    """
    判断是否存在文本信息
    :param text: 要判断的文本信息
    :return: True or False
    """
    try:
        xpath = '//*[contains(text(), "{}")]'.format(text)
        element = DriverUtil.get_driver().find_element_by_xpath(xpath)
        return element is not None
    except Exception:
        return False


def switch_to_frame(data, dr=1):
    """
    切换网页内窗口
    :param data: frame ID 或者 frame name
    :param dr: dr=1 切换至新frame  dr=2 切换回上一级frame dr=3 切换至父级frame
    :return:
    """
    driver = DriverUtil.get_driver()

    if dr == 1:
        driver.switch_to.frame(data)

    elif dr == 2:
        data = ""
        driver.switch_to.parent_frame()
    elif dr == 3:

        driver.switch_to.default_content()


class DriverUtil(object):
    """定义浏览器工具类"""

    _driver = None

    # 添加自动退出标记
    _auto_quit = True

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        if cls._driver is None:
            # 初始化浏览器对象
            cls._driver = webdriver.Chrome()
            # 设置窗口最大化
            cls._driver.maximize_window()
            # 设置隐式等待
            cls._driver.implicitly_wait(10)
            # 打开链接
            cls._driver.get('https://mail.qq.com/')
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        if cls._auto_quit and cls._driver:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def auto_quit(cls, auto_quit):
        """开关浏览器退出方法"""
        cls._auto_quit = auto_quit
