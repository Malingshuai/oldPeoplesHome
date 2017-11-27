# -*- coding: utf-8 -*-
"""
编写目的：实现后台登录页面的元素定位，并提供每个元素操作方法，模拟用户操作
编写时间：2017-11-25
"""
from selenium.webdriver.common.by import By
from base import Page

class backlogin(Page):
    """后台管理登录页面"""
    back_login_username = (By.ID, "mobile-value")
    back_login_password = (By.ID, "password")
    back_login_login = (By.CLASS_NAME, "login-btn")

    def input_username(self, username):
        self.find_elemet(*self.back_login_username).clear()
        self.find_elemet(*self.back_login_username).send_keys(username)

    def input_password(self, password):
        self.find_elemet(*self.back_login_password).clear()
        self.find_elemet(*self.back_login_password).send_keys(password)

    def click_login(self):
        self.find_elemet(*self.back_login_login).click()


    def adminLogin(self, usname="17600603558", password="17600603558"):
        """""超级管理登录"""
        self.open()
        try:
            self.input_username(usname)
            self.input_password(password)
            self.click_login()
            self.driver.implicitly_wait(5)
        except:
            sleep(6)
            self.input_username(usname)
            self.input_password(password)
            self.click_login()
            self.driver.implicitly_wait(5)

    login_namepass_error = (By.XPATH, '//*[@id="ember732"]/div[5]/section/div[2]/div/div[2]/span[3]')
    login_userexists_error = (By.XPATH, '//*[@id="ember732"]/div[5]/section/div[2]/div/div[2]/span[2]')

    def get_error(self):
        try:
            return self.find_elemet(*self.login_userexists_error).text
        except:
            return self.find_elemet(*self.login_namepass_error).text

if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep
    driver = webdriver.Chrome()
    a = backlogin(driver, "http://web.tnb99.net/index.html")
    # windows = driver.current_window_handle
    a.adminLogin()
    print a.get_error()
    sleep(5)
    driver.quit()