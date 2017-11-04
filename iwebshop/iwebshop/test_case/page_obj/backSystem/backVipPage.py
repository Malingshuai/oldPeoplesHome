# -*- coding: utf-8 -*-
"""
编写目的：实现后台首页页面的元素定位，
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
from iwebshop.iwebshop.test_case.page_obj.backSystem import backHomePage

class backvip(backHomePage.backhome):
    """实现会员TAB页的菜单选择"""
    backvip_catalog_viplist = (By.LINK_TEXT, u"会员列表")
    backvip_catalog_vipslist = (By.LINK_TEXT, u"会员组列表")
    backvip_catalog_viptixian = (By.LINK_TEXT, u"会员提现管理")
    backvip_catalog_jianyiguanli = (By.LINK_TEXT, u"建议管理")
    backvip_catalog_zixunguanli = (By.LINK_TEXT, u"咨询管理")
    backvip_catalog_taolunguanli = (By.LINK_TEXT, u"讨论管理")
    backvip_catalog_pingjiaguanli = (By.LINK_TEXT, u"评价管理")
    backvip_catalog_zhanneixiaoxi = (By.LINK_TEXT, u"站内消息")
    backvip_catalog_daohuotongzhi = (By.LINK_TEXT, u"到货通知")
    backvip_catalog_mubanguanli = (By.LINK_TEXT, u"模板管理")
    backvip_catalog_youjianguanli = (By.LINK_TEXT, u"邮件订阅")

    def click_backvip_viplis(self):
        """进入会员管理界面"""
        self.find_elemet(*self.backvip_catalog_viplist).click()

    def click_backvip_vipslit(self):
        """进入会员组管理"""
        self.find_elemet(*self.backvip_catalog_vipslist).click()

    def click_backvip_viptixian(self):
        """进入会员提现管理"""
        self.find_elemet(*self.backvip_catalog_viptixian).click()

    def click_backvip_jianyiguanli(self):
        """进入建议管理界面"""
        self.find_elemet(*self.backvip_catalog_jianyiguanli).click()

    def click_backvip_zixunguanli(self):
        """进入咨询管理界面"""
        self.find_elemet(*self.backvip_catalog_taolunguanli).click()

    def click_backvip_pingjiaguanli(self):
        """进入评价管理界面"""
        self.find_elemet(*self.backvip_catalog_pingjiaguanli).click()

    def click_backvip_zhanneixiaoxi(self):
        """进入站内消息界面"""
        self.find_elemet(*self.backvip_catalog_zhanneixiaoxi).click()

    def click_backvip_daohuotongzhi(self):
        """进入到货通知界面"""
        self.find_elemet(*self.backvip_catalog_daohuotongzhi).click()

    def click_backvip_mubangauanli(self):
        """进入模板管理界面"""
        self.find_elemet(*self.backvip_catalog_mubanguanli).click()

    def click_backvip_youjiandingyue(self):
        """进入模板订阅界面"""
        self.find_elemet(*self.backvip_catalog_youjianguanli).click()

class viplist(backvip):
    """添加会员、全选、批量删除、批量编辑、回收站、筛选、预付款、搜索"""
    viplist_addvip = (By.XPATH, '//*[@id="admin_right"]/div/div[2]/a[1]/button/span')
    viplist_selectedall = (By.XPATH, '//*[@id="admin_right"]/div/div[2]/a[2]/button/span')
    viplist_deleteall = (By.CLASS_NAME, "delete")

    def click_viplist_selectedall(self):
        self.find_elemet(*self.viplist_selectedall).click()

    def click_viplist_deleteall(self):
        self.find_elemet(*self.viplist_deleteall).click()

    delete_windows_yes = (By.ID, "artPlusConfirmyes")

    def delete_windowsyes(self):
        self.find_elemet(*self.delete_windows_yes).click()

if __name__ == '__main__':
    from selenium import webdriver
    from iwebshop.iwebshop.test_case.models.function import insert_img
    driver = webdriver.Chrome()
    a=viplist(driver, "http://localhost/iwebshop/index.php?controller=systemadmin&action=index")
    a.adminLogin()
    a.click_backhome_vip()
    driver.implicitly_wait(5)
    a.click_viplist_selectedall()
    a.click_viplist_deleteall()
    print u"准备删除所有会员！"
    a.delete_windowsyes()
    print u"删除全部会员成功！截图显示"
    insert_img(a.driver, u"全部会员删除成功.jpg")
    driver.quit()