# coding=utf-8
"""用例初始，setup() 和 tearDown()"""

from iwebshop.test_case.models.driver import browser
import unittest

class MyTest(unittest.TestCase):
    """初始化，获取浏览器操作句柄"""
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()