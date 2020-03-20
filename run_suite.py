import unittest

from script.test_login import TestLogin
from script.test_return import TestReturn
from script.test_write import TestWrite
from tools.HTMLTestReportCN import HTMLTestRunner
import config

from utils import DriverUtil

# 初始化测试套件对象


suite = unittest.TestSuite()

# 组装测试用例

suite.addTest(unittest.makeSuite(TestLogin))  # 登陆
# suite.addTest(unittest.makeSuite(TestWrite))#写
# suite.addTest(unittest.makeSuite(TestReturn))#读

# 关掉浏览器退出方法
DriverUtil.auto_quit(False)

# 调用执行套件对象
# unittest.TextTestRunner().run(suite)

# 设置报告存放路径及文件名
report_path = config.BASE_DIR + '/report/' + 'QQEmail.html'

# 打开报告写入文件流
with open(report_path, 'wb') as f:
    # 初始化测试执行对象
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title='Asimov Web自动化测试报告',
                            description='系统: macOS, 浏览器: 谷歌浏览器 脚本语言: Python',
                            tester='QA')
    # 调用执行方法
    runner.run(suite)

# 打开浏览器退出方法
DriverUtil.auto_quit(True)

# 退出浏览器对象
DriverUtil.quit_driver()
