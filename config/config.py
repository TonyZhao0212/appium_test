from appium import webdriver

class server_conf():
    def initial_conf(self):
        self.desired_caps = {}
        self.desired_caps['deviceName'] = 'MHA-AL00'
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '9'
        self.desired_caps['appPackage'] = 'com.taobao.taobao'
        self.desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'
        self.desired_caps['unicodeKeyboard'] = 'true' # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
        self.desired_caps['resetKeyboard'] = 'true' # 是否在测试结束后将键盘重轩为系统默认的输入法。
        self.desired_caps['noReset'] = True # true:不重新安装APP，false:重新安装app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.desired_caps)
        self.driver.implicitly_wait(40)
        return self.driver