# -*- coding: utf-8 -*-
"""
编写目的：实现后台首页title和导航栏元素定位，
1.click_backhome_shop() 进入商品管理TAB页
2.click_backhome_vip() 进入会员管理TAB页
3.click_backhome_dingdan() 进入订单管理TAB页
4.click_backhome_yingxiao() 进入营销管理TAB页
5.click_backhome_system() 进入系统管理TAB页
6.click_backhome_tools() 进入工具管理TAB页
7.click_backhome_iwebshophome() 进入前台首页
8.click_backhome_logout（） 退出登录状态
9.get_backhome_user（） 获取当前登录用户名
编写时间：2017-03-19
"""
from selenium.webdriver.common.by import By
from iwebshop.test_case.page_obj.backSystem.backLoginPage import backlogin

class backhome(backlogin):
    """提供后台首页title和导航功能：导航（商品、会员、订单、营销、统计、系统、工具、退出管理）"""
    back_home_shop = (By.LINK_TEXT, u"商品")
    back_home_vip = (By.LINK_TEXT, u"会员")
    back_home_dingdan = (By.LINK_TEXT,u"订单")
    back_home_yingxiao = (By.LINK_TEXT, u"营销")
    back_home_system = (By.LINK_TEXT, u"系统")
    back_home_tools = (By.LINK_TEXT, u"工具")
    back_home_iwebshophome = (By.LINK_TEXT, u"商城首页")
    back_home_backhome = (By.LINK_TEXT, u"后台首页")
    back_home_logout = (By.LINK_TEXT, u"退出管理")
    back_home_Logo = (By.XPATH, '//*[@id="header"]/div[1]/a/img')
    back_home_username = (By.CSS_SELECTOR, u"#header > p > span > label:nth-child(1)")

    def click_backhome_shop(self):
        '''进入到商品管理界面'''
        self.find_elemet(*self.back_home_shop).click()

    def click_backhome_vip(self):
        '''进入到会员管理界面'''
        self.find_elemet(*self.back_home_vip).click()

    def click_backhome_dingdan(self):
        '''进入到订单管理界面'''
        self.find_elemet(*self.back_home_dingdan).click()

    def click_backhome_yingxiao(self):
        '''进入到营销管理界面'''
        self.find_elemet(*self.back_home_yingxiao).click()

    def click_backhome_system(self):
        '''进入到系统管理界面'''
        self.find_elemet(*self.back_home_system).click()

    def click_backhome_tools(self):
        '''进入到工具管理界面'''
        self.find_elemet(*self.back_home_tools).click()

    def click_backhome_iwebshophome(self):
        '''进入到商城前台首页'''
        self.find_elemet(*self.back_home_iwebshophome).click()

    def click_backhome_logout(self):
        '''退出后台管理系统'''
        self.find_elemet(*self.back_home_logout).click()

    def get_backhome_user(self):
        '''获取当前登录后台系统用户信息'''
        return self.find_elemet(*self.back_home_username).text
