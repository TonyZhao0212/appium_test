from cProfile import run
from unittest import TestLoader, runner
from appium import webdriver
from test_case import searchtest
import time,unittest,HtmlTestRunner

def suite():
    #test1 = TestLoader().loadTestsFromTestCase(testcase1.testAction)
    test1 = TestLoader().loadTestsFromTestCase(searchtest.testAction)
    suite = unittest.TestSuite(test1)
    return suite

if __name__ == '__main__':
    runner=HtmlTestRunner.HTMLTestRunner()
    runner.run(suite())
