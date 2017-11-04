# -*- coding: utf-8 -*-
"""
编写目的：实现前台商品详情页面的元素定位，并提供每个元素操作方法，模拟用户选择商品
编写时间：2016-10-17
"""

from selenium.webdriver.common.by import By

from iwebshop.iwebshop.test_case.page_obj.base import Page


class showhome(Page):
    '''前台用户登录页面'''

    # 定位
    shop_yanse = (By.ID, "a238f22baaa5197c38b3ca0c2d4792fb")        # 商品颜色
    shop_chima = (By.ID, "e737584ec6ea30637b1e2b1dde624fbe")        # 商品尺码
    shop_shuliang = (By.ID, "number")                               # 购买商品数量
    shop_lijigoumai = (By.ID, "buy_now")                            # 立即购买按钮
    shop_details_tishi = (By.ID, "artPlustipscontent")               # 点击立即购买后的提示信息


    # 点击商品，颜色
    def details_yanse(self):
        return self.find_elemet(*self.shop_yanse).click()

    # 点击商品，尺码
    def details_chima(self):
        return self.find_elemet(*self.shop_chima).click()

    # 立即购买
    def details_shuliang(self):
        return self.find_elemet(*self.shop_shuliang).send_keys("1")

    # 点击商品，颜色
    def details_lijigoumai(self):
        return self.find_elemet(*self.shop_lijigoumai).click()

    # 同意购买商品入口
    def details_shop(self):
        self.details_yanse()
        self.details_chima()
        self.details_lijigoumai()
        driver.implicitly_wait(5)




if __name__ == '__main__':
    from selenium import webdriver
    from iwebshop.iwebshop.test_case.page_obj.frontSystem.showhomePage import showhome

    driver = webdriver.Chrome()


    a = showhome(driver, "http://127.0.0.1/iwebshop/")
    a.click_shop()

