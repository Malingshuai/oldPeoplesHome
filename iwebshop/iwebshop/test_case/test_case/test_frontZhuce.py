# -*- coding: utf-8 -*-
"""
编写目的：前台注册功能测试
编写时间：2017-03-21
"""
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from iwebshop.test_case.models import myunit, function
from ddt import ddt, data, unpack
from iwebshop.test_case.models.GetData import get_csv_data
from iwebshop.test_case.page_obj.frontSystem.zhucePage import zhuce
from iwebshop.test_case.page_obj.frontSystem.loginPage import login


@ddt
class frontZhuceTest(myunit.MyTest):
    """前台注册功能测试"""
    @data(*get_csv_data('D:\projectTestCase\iwebshop\iwebshop\data\data.csv'))
    @unpack
    def test_azhuce(self, emil, username, password, repassword):
        """注册用户"""
        browes = zhuce(self.driver, "http://127.0.0.1/iwebshop/")
        browes.user_zhuce(emil, username, password, repassword)
        self.driver.implicitly_wait(5)
        result = browes.get_zhuce_success()
        self.assertEqual(result, u"恭喜，操作成功！")


@ddt
class frontlogin(myunit.MyTest):
    """前台登录功能测试"""
    @data(*get_csv_data('D:\projectTestCase\iwebshop\iwebshop\data\logindata.csv'))
    @unpack
    def test_blogin(self, username, password):
        """用户登录"""
        browes = login(self.driver, "http://127.0.0.1/iwebshop/")
        browes.userLogin(username, password)
        result = browes.get_anquantuichu()
        self.assertEqual(result, u"安全退出")
