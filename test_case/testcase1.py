#from appium import webdriver
import unittest,time
from config import config
from operation import guesture
import subprocess

class testAction(unittest.TestCase):
    def setUp(self):
        self.driver = config.server_conf.initial_conf(self)
    def test_01(self):
        pi = 'adb shell pm clear com.taobao.taobao'
        clear_result = subprocess.Popen(pi,shell=True,stdout=subprocess.PIPE)
        print(clear_result.stdout.read())
        time.sleep(5)
    def test_02(self):
        self.driver.find_element_by_id('com.taobao.taobao:id/provision_positive_button').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.taobao.taobao:id/txtConfirm').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
    def test_03(self):
        time.sleep(15)
        for i in range(2):
            guesture.guesture.swipe_up(self,self.driver)
            time.sleep(2)
            guesture.guesture.swipe_down(self,self.driver)
            time.sleep(2)
            guesture.guesture.swipe_left(self,self.driver)
            time.sleep(2)
            guesture.guesture.swipe_right(self,self.driver)
            time.sleep(2)
    def tearDown(self):
        self.driver.quit()

'''if __name__ == '__main__':
unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner()) '''
