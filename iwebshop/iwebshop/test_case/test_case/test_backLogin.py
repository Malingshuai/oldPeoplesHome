# -*- coding: utf-8 -*-
"""测试目的：iwebshop后台登录场景测试用例
编写时间：2016-10-15
"""
import sys
import unittest
# 将文件路径添加到运行环境变量，方便程序查找
sys.path.append("../models")
sys.path.append("../page_obj")
from test_case.models import myunit, function
from test_case.page_obj.backSystem.backLoginPage import backlogin
from test_case.page_obj.backSystem.backHomePage import backhome

class backLoginTest(myunit.MyTest):
    """iwebshop后台登录功能测试"""

    def test_login1(self):
        """"验证账号为空登录功能"""
        po = backlogin(self.driver, "http://localhost/iwebshop/index.php?controller=systemadmin&action=index")
        po.adminLogin('', '1234567')
        self.assertEqual(po.get_error(), u"登录名不能为空", msg="测试不通过！")
        function.insert_img(self.driver, u"登录名不能为空.jpg")

    def test_login2(self):
        """"账号正确，密码为空"""
        po = backlogin(self.driver, "http://localhost/iwebshop/index.php?controller=systemadmin&action=index")
        po.adminLogin('admin','')
        self.assertEqual(po.get_error(), u"密码不能为空", msg="测试不通过！")
        function.insert_img(self.driver, u"密码不能为空.jpg")

    def test_login3(self):
        """"账号不存在"""
        po = backlogin(self.driver, "http://localhost/iwebshop/index.php?controller=systemadmin&action=index")
        po.adminLogin('123456', '123456')
        self.assertEqual(po.get_error(), u"用户名与密码不匹配", msg="测试不通过！")
        function.insert_img(self.driver, u"用户名与密码不匹配.jpg")

    def test_login4(self):
        """"账号正确，密码正确"""
        po = backhome(self.driver, "http://localhost/iwebshop/index.php?controller=systemadmin&action=index")
        po.adminLogin()
        self.assertEqual(po.get_backhome_user(), "admin", msg="测试不通过！")
        function.insert_img(self.driver, u"登录成功.jpg")


if __name__ == '__main__':
    try:
        suite = unittest.TestSuite()
        suite.addTest(backLoginTest("test_login1"))
        suite.addTest(backLoginTest("test_login2"))
        suite.addTest(backLoginTest("test_login3"))
        suite.addTest(backLoginTest("test_login4"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    except:
        print "元素无法定位"
