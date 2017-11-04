# coding=utf-8
"""测试目的：iwebshop后台登录场景测试用例
编写时间：2016-10-15
"""
import sys
import os
import unittest

# 将文件路径添加到运行环境变量，方便程序查找
path = os.path.dirname(os.getcwd())  # 获取上级目录
path1 = path + "\\models"
path2 = path + "\\page_obj"
sys.path.append(path1)
sys.path.append(path2)
from iwebshop.test_case.models import myunit, function, driver
from iwebshop.test_case.page_obj.backSystem.backLoginPage import backlogin
from iwebshop.test_case.page_obj.backSystem.backSystemPage import JiBenSheZhi, BackSystem
from selenium.common.exceptions import NoSuchElementException
from ddt import ddt, unpack, data
from iwebshop.test_case.models.GetData import get_csv_data


@ddt
class BackSystemWZSZ(myunit.MyTest):
    """iwebshop后系统设置中网站设置"""

    def setUp(self):
        self.driver = driver.browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        backlogin(self.driver, 'http://localhost/iwebshop/index.php?controller=systemadmin&action=index').adminLogin()

    @data(*get_csv_data("D:/projectTestCase/iwebshop/iwebshop/data/backSystemJBSZ.csv"))
    @unpack
    def test_JiBenSheZhi(self, *valus):
        """"验证网站基本设置"""
        try:
            cd = BackSystem(self.driver)
            cd.click_wangzhanguanli()
            jd = JiBenSheZhi(cd.driver)
            jd.input_shangdianName(valus[1])
            jd.input_shangdiandizhi(valus[2])
            jd.input_shangdianlogo(valus[3])
            jd.input_lianxiren(valus[4])
            jd.input_QQ(valus[5])
            jd.input_email(valus[6])
            jd.input_mobile(valus[7])
            jd.input_phone(valus[8])
            jd.input_jutidizhi(valus[9])
            jd.input_huohaoqianzhui(valus[10])
            jd.input_titleHouZhui(valus[11])
            jd.click_submit()
            self.assertEqual(jd.get_prompt_txt(), unicode(valus[14], "gbk"), msg=u"测试不通过！")
            function.insert_img(self.driver, u"登录名不能为空.jpg")
        except NoSuchElementException:
            print(u'元素获取失败！')


if __name__ == '__main__':
    try:
        suite = unittest.TestSuite()
        suite.addTest(BackSystemWZSZ("test_JiBenSheZhi"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    except:
        print "元素无法定位"
