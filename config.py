import os
import logging.handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 工程根目录


# print(os.path.dirname(os.path.abspath(__file__)))
# print("====", os.path.abspath(__file__))
# print(">>>>", __file__)

def init_log_config():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(level=logging.INFO)
    # 创建处理器
    # 输出到控制台的处理器
    sh = logging.StreamHandler()
    log_path = BASE_DIR + '/log/' + 'QQEmail.log'
    # 输出到文件的处理器
    th = logging.handlers.TimedRotatingFileHandler(log_path,
                                                   when='midnight',
                                                   interval=1,
                                                   backupCount=5,
                                                   encoding='utf-8')

    # 创建格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    # 将格式器添加给处理器
    sh.setFormatter(formatter)
    th.setFormatter(formatter)

    # 将处理器添加给日志器
    logger.addHandler(sh)
    logger.addHandler(th)
