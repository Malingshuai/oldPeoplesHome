# coding=utf-8
"""
1.页面基类，所有页面均继承该类；
2.find_elemet() 方法用于定位页面单个元素；
3.find_elemets() 方法用于批量定位页面元素；
4.open() 方法用于打开指定URL；
5.script()方法用于调用JavaScript代码；
"""
class Page(object):
    """页面基础类，用于所有页面的继承, 用于打开网站"""

    bbs_url = 'http://localhost/iwebshop/index.php?controller=systemadmin&action=index'

    # 需传 浏览器操作句柄，URL，超时等待时间
    def __init__(self, selenium_drive, base_url=bbs_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_drive
        self.timeout = 30
        self.parent = parent

    def __open(self):
        url = self.base_url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def find_elemet(self, *loc):
        return self.driver.find_element(*loc)

    def find_elemets(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self.__open()

    def on_page(self):
        return self.driver.current_url == self.base_url

    def scripr(self, src):
        return self.driver.execute_script(src)