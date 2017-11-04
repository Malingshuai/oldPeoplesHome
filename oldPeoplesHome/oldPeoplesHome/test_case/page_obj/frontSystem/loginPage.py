# -*- coding: utf-8 -*-
"""
编写目的：实现前台用户登录
input_username() 方法输入用户名
input_password() 方法输入密码
click_jizhuUsername() 方法勾选记住密码
click_findpassword() 点击忘密码
click_login()   点击登录按钮
编写时间：2016-10-17
"""
from selenium.webdriver.common.by import By
from iwebshop.iwebshop.test_case.page_obj.frontSystem import showhomePage

class login(showhomePage.showhome):
    """实现用户登录"""
    login_username = (By.NAME, "login_info")                  # 用户名
    login_password = (By.NAME, "password")                    # 密码
    login_jizhuusername = (By.NAME, "remember")               # 记住登录名
    login_findpassword = (By.LINK_TEXT, u"忘记密码")          # 忘记密码
    login_batten = (By.CLASS_NAME, "submit_login")            # 登录按钮

    def input_login_username(self, username):
        """输入用户名"""
        self.find_elemet(*self.login_username).clear()
        self.find_elemet(*self.login_username).send_keys(username)

    def input_login_password(self, password):
        """输入密码"""
        self.find_elemet(*self.login_password).clear()
        self.find_elemet(*self.login_password).send_keys(password)

    def click_login_jizhuUsername(self, username):
        """勾选/取消记住登录名"""
        self.find_elemet(*self.login_jizhuusername).click()

    def click_login_findpassword(self):
        """忘记密码"""
        self.find_elemet(*self.login_findpassword).click()

    def login_click_login(self):
        self.find_elemet(*self.login_batten).click()

    def userLogin(self, username="test_001", password="123456"):
        """"" 输入用户名密码登录 """
        self.open()
        self.click_homeLoginBatten()
        self.driver.implicitly_wait(5)
        self.input_login_username(username)
        self.input_login_password(password)
        self.login_click_login()
        self.driver.implicitly_wait(5)

    login_username_warning = (By.XPATH, "/html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/label")
    login_password_warning = (By.XPATH, '/html/body/div[1]/div[2]/div/div/form/table/tbody/tr[2]/td/label')
    login_warning = (By.XPATH, "/html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/div")

    def get_warning(self):
        """获取登录失败提示语"""
        try:
            warning = self.find_elemet(*self.login_warning).text
        except:
            try:
                warning = self.find_elemet(*self.login_password_warning).text
            except:
                warning = self.find_elemet(*self.login_username_warning).text
        finally:
            return warning


class findPassword(login):
    """忘记密码"""
    findPassword_username = (By.ID, "username")
    findPassword_email = (By.ID, "useremail")
    findPassword_submit = (By.CLASS_NAME, "submit")

    def input_findPassword_username(self, username):
        self.find_elemet(*self.findPassword_username).clear()
        self.find_elemet(*self.findPassword_username).send_keys(username)

    def input_findPassword_emil(self, useremil):
        self.find_elemet(*self.findPassword_email).clear()
        self.find_elemet(*self.findPassword_email).send_keys(useremil)

    def click_findPassword_submit(self):
        self.find_elemet(*self.findPassword_submit).click()

    login_alert = (By.ID, 'artPlustipscontent')

    def get_alert(self):
        return self.find_elemet(*self.login_alert).text

    def findPassword(self, username, emil):
        self.open()
        self.click_homeLoginBatten()
        self.driver.implicitly_wait(5)
        self.click_login_findpassword()
        self.input_findPassword_username()
        self.input_findPassword_emil()
        self.click_findPassword_submit()
        print self.get_alert()


if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep
    driver = webdriver.Chrome()
    a = findPassword(driver, "http://127.0.0.1/iwebshop/")
    a.userLogin("user", "")
    print a.get_warning()
    sleep(5)
    driver.quit()
