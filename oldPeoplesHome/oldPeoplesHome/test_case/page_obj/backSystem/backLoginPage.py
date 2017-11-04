# -*- coding: utf-8 -*-
"""
编写目的：实现后台登录页面的元素定位，并提供每个元素操作方法，模拟用户操作
编写时间：2016-10-15
"""
from selenium.webdriver.common.by import By
from iwebshop.test_case.page_obj.base import Page

class backlogin(Page):
    """后台管理登录页面"""
    back_login_username = (By.NAME, "admin_name")
    back_login_password = (By.NAME, "password")
    back_login_login = (By.XPATH, "//*[@id='wrapper']/div/div[2]/form/table/tbody/tr[3]/td/input[1]")
    back_login_quxiao = (By.XPATH, "//*[@id='wrapper']/div/div[2]/form/table/tbody/tr[3]/td/input[2]")

    def back_input_username(self, username):
        self.find_elemet(*self.back_login_username).send_keys(username)

    def back_input_password(self, password):
        self.find_elemet(*self.back_login_password).send_keys(password)

    def back_click_login(self):
        self.find_elemet(*self.back_login_login).click()

    def back_click_quxiao(self):
        self.find_elemet(*self.back_login_quxiao).click()

    def adminLogin(self, usname="admin", password="123456"):
        """""超级管理登录"""
        self.open()
        self.back_input_username(usname)
        self.back_input_password(password)
        self.back_click_login()
#       sleep(1)
        self.driver.implicitly_wait(5)

    back_login_error = (By.ID, "artPlustipscontent")

    def get_error(self):
        return self.find_elemet(*self.back_login_error).text

if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep
    driver = webdriver.Chrome()
    a = backlogin(driver,"http://localhost/iwebshop/index.php?controller=systemadmin&action=index")
    # windows = driver.current_window_handle
    a.adminLogin()
    print a.get_error()
    sleep(5)
    driver.quit()