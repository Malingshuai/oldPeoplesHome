# !/usr/bin/env python
# -*- coding: utf8 -*-
"""移动端测试用例样板
"""


import unittest
from appium import webdriver
from ddt import ddt, data, unpack
from time import sleep
import codecs
from GetData import get_csv_data

@ddt
class TestScenario(unittest.TestCase):
    """ inheriting the TestCase class"""

    @classmethod
    def setUpClass(cls):
        """test preparation"""
        cls.desired_caps={}
        cls.desired_caps['platformName']='Android'
        cls.desired_caps['platformVersion']='4.3'
        cls.desired_caps['deviceName']='192.168.56.101:5555'
        cls.desired_caps['appPackage']='com.example.zhangjian.minibrowser2'
        cls.desired_caps['appActivity']='com.example.zhangjian.minibrowser2.myapplication.MainActivity'
        cls.desired_caps["unicodeKeyboard"] = "True"
        cls.desired_caps["resetKeyboard"] = "True"
        #self.desired_caps["automationName"] = "Selendroid"
        cls.driver=webdriver.Remote('http://localhost:4723/wd/hub',cls.desired_caps)

    @data(*get_csv_data('./data/data.csv'))
    @unpack
    def test_search(cls, target_url, search_value):
        """test case for scenario a"""
        elem = cls.driver.find_element_by_id('url')
        search_value = search_value.decode('unicode_escape')
        print search_value
        elem.send_keys(search_value)
        sleep(2)
        btn = cls.driver.find_element_by_id('searchbutton')
        btn.click()
        sleep(3)
        ctn = cls.driver.find_element_by_id('clearbutton')
        ctn.click()
        cls.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()