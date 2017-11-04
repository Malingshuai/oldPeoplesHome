# -*- coding: utf-8 -*-
"""
编写目的：实现前台首页页面的元素定位，
1.
编写时间：2016-10-17
"""
from selenium.webdriver.common.by import By
from iwebshop.iwebshop.test_case.page_obj.base import Page

class showhome(Page):
    """提供登录、注册、我的账户、我的订单点击操作、安全退出"""
    myzhanghu = (By.LINK_TEXT, u"我的账户")
    mydingdan = (By.LINK_TEXT, u"我的订单")
    shiyongbangzhu = (By.LINK_TEXT, u"使用帮助")
    homeLoginBatten = (By.LINK_TEXT, u"登录")
    mianfeizhuce = (By.LINK_TEXT, u"免费注册")
    anquantuichu = (By.LINK_TEXT, u"安全退出")
    titleLogoiwebshop = (By.LINK_TEXT,"iwebshop")

    def click_myzhanghu(self):
        """进入我的账户"""
        self.find_elemet(*self.myzhanghu).click()

    def click_mydingdan(self):
        """进入我的订单"""
        self.find_elemet(*self.mydingdan)

    def click_shiyongbangzhu(self):
        """进入使用帮助"""
        self.find_elemet(*self.shiyongbangzhu).click()

    def click_homeLoginBatten(self):
        """进入登录界面"""
        self.find_elemet(*self.homeLoginBatten).click()

    def click_mianfeizhuce(self):
        """进入免费注册界面"""
        self.find_elemet(*self.mianfeizhuce).click()

    def get_anquantuichu(self):
        """监测到安全退出后返回安全退出"""
        return self.find_elemet(*self.anquantuichu).text

    def click_anquantuichu(self):
        """退出登录"""
        self.find_elemet(*self.anquantuichu).click()

    def click_titleLogo(self):
        """点击logo"""
        self.find_elemet(*self.titleLogoiwebshop).click()

    def click_shop(self):
        """选择商品进入商品详情界面"""
        home_shoplist = (By.TAG_NAME, "p")
        home_shoplist_element = self.find_elemets(*home_shoplist)
        shops = []
        for i in home_shoplist_element:
            if i.get_attribute('class') == 'pro_title':
                shops.append(i)
        return shops


if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep
    driver = webdriver.Chrome()
    a = showhome(driver, "http://127.0.0.1/iwebshop/")
    a.open()
    driver.implicitly_wait(5)
    list = a.click_shop()
    print list
    print len(list)
    list[25].click()
    sleep(5)
    driver.quit()
