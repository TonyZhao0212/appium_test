import unittest,time
from config import config
from operation import guesture
import subprocess

class testAction(unittest.TestCase):
    def setUp(self):
        self.driver = config.server_conf.initial_conf(self)
    def test_search(self):
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="搜索"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('com.taobao.taobao:id/search_bar_wrapper').click()
        time.sleep(2)
        searchbox = self.driver.find_element_by_id('com.taobao.taobao:id/searchEdit')
        searchbox.send_keys('nike')
        time.sleep(2)
        self.driver.find_element_by_id('com.taobao.taobao:id/searchbtn').click()
        time.sleep(5)
        #guesture.guesture.swipe_down(self,self.driver)
        time.sleep(2)
        self.driver.find_element_by_id('com.taobao.taobao:id/styleBtn').click()
    def tearDown(self):
        self.driver.quit()

'''if __name__ == '__main__':
unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner()) '''
