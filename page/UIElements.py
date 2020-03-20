from selenium.webdriver.common.by import By


class UIElements:
    """管理所有页面元素"""

    """qq邮箱登陆页面"""

    Account_password_login_btn = (By.ID, 'switcher_plogin')  # 账号密码登陆按钮

    input_user_name = (By.ID, 'u')  # 账号输入框

    input_password = (By.ID, 'p')  # 密码输入框

    login_button = (By.ID, 'login_button')  # 登录按钮

    """qq邮箱首页"""

    write_a_letter_btn = (By.XPATH, '//*[@id="composebtn"]')  # 写信按钮

    inbox_btn = (By.ID, 'folder_1')  # 收件箱按钮

    """写信页面"""

    Recipient_input_box = (By.XPATH, "//*[@id='toAreaCtrl']/div[2]/input")  # 收件人输入框

    Subject_input_box = (By.ID, 'subject')  # 主题输入框

    text_input = (By.XPATH, '/html/body')  # 正文输入框

    send_btn = (By.XPATH, '//*[@id="toolbar"]/div/a[1]')  # 发送按钮

    Return_homepage = (By.ID, 'btnbackl')  # 返回邮箱首页按钮

    """收件箱页面"""

    apple_email = (
        By.XPATH, '//*[@id="div_showlastweek"]/table[1]/tbody/tr/td[3]/table/tbody/tr/td[1]/nobr/span')  # 具体邮件
    user_email = (
        By.XPATH, '//*[@id="mailContentContainer"]/table/tbody/tr/td/div[1]/table/tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td[1]/a') #页面邮箱号元素
