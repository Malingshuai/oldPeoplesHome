# -*- coding: utf-8 -*-
"""
编写目的：实现前台注册页面的元素定位，并提供每个元素操作方法，模拟用户操作
编写时间：2016-10-16
"""
from selenium.webdriver.common.by import By
from iwebshop.iwebshop.test_case.page_obj.frontSystem import  showhomePage

class zhuce(showhomePage.showhome):
    '''前台用户注册页面'''

    zhuce_emile = (By.NAME, "email")                             # 注册邮箱
    zhuce_username = (By.NAME, "username")                       # 注册用户名
    zhuce_password = (By.NAME, "password")                       # 注册密码
    zhuce_repassword = (By.NAME, "repassword")                   # 确认密码
    zhuce_submit = (By.CLASS_NAME, "submit_reg")                 # 同意以下条款，提交
    zhuce_success = (By.XPATH, "/html/body/div[1]/div[2]/div/div/table/tbody/tr/td/p[1]/strong")
    zhuce_error = (By.ID, 'artPlustipscontent')

    def input_zhuce_emile(self, emile):
        """注册界面，输入邮箱"""
        self.find_elemet(*self.zhuce_emile).clear()
        self.find_elemet(*self.zhuce_emile).send_keys(emile)

    def input_zhuce_username(self, username):
        """注册界面，输入用户名"""
        self.find_elemet(*self.zhuce_username).clear()
        self.find_elemet(*self.zhuce_username).send_keys(username)

    def input_zhuce_password(self, password):
        """注册界面，输入密码"""
        self.find_elemet(*self.zhuce_password).clear()
        self.find_elemet(*self.zhuce_password).send_keys(password)

    def input_zhuce_repassword(self, repassword):
        """注册界面，输入确认密码"""
        self.find_elemet(*self.zhuce_repassword).clear()
        self.find_elemet(*self.zhuce_repassword).send_keys(repassword)

    def click_zhuce_submit(self):
        """注册界面，同意以下条款，提交"""
        self.find_elemet(*self.zhuce_submit).click()

    def user_zhuce(self, emile, username, password, repassword):
        """"" 注册用户 """
        self.open()
        self.click_mianfeizhuce()
        self.driver.implicitly_wait(5)
        self.input_zhuce_emile(emile)
        self.input_zhuce_username(username)
        self.input_zhuce_password(password)
        self.input_zhuce_repassword(repassword)
        self.click_zhuce_submit()
        self.driver.implicitly_wait(5)

    def get_zhuce_success(self):
        """验证注册成功"""
        return self.find_elemet(*self.zhuce_success).text

    error_emil = (By.XPATH, "/html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/label")
    error_username = (By.XPATH, "/html/body/div[1]/div[2]/div/div/form/table/tbody/tr[2]/td/label")
    error_password = (By.XPATH, "/html/body/div[1]/div[2]/div/div/form/table/tbody/tr[3]/td/label")
    error_repassword = (By.XPATH, "/html/body/div[1]/div[2]/div/div/form/table/tbody/tr[4]/td/label")

    def get_error_emil(self):
        """获取Emil错误提示"""
        return self.find_elemet(*self.error_emil).text

    def get_error_username(self):
        """获取username错误提示"""
        return self.find_elemet(*self.error_username).text

    def get_error_password(self):
        """获取password错误提示"""
        return self.find_elemet(*self.error_password).text

    def get_error_repassword(self):
        """获取确认密码错误提示"""
        return self.find_elemet(*self.error_repassword).text

    def get_zhuce_error(self):
        """获取注册失败提示信息"""
        return self.find_elemet(*self.zhuce_error).text

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    a = zhuce(driver, "http://127.0.0.1/iwebshop/")
    a.user_zhuce("", "user011", "123456", "12356")
    errors = [a.error_emil, a.error_username, a.error_password, a.error_repassword]
    for keys in errors:
        try:
            if keys == a.error_emil:
                print a.get_error_emil()
            elif keys == a.error_username:
                print a.get_error_username()
            elif keys == a.error_password:
                print a.get_error_password()
            else:
                print a.get_error_repassword()
        except:
            pass
    try:
        print a.get_zhuce_error()
    except:
        pass
    driver.quit()
