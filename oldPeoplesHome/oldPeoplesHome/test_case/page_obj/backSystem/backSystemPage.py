# coding=utf-8
"""
编写目的：实现后台系统管理的元素定位，
编写时间：2017-03-19
"""
from selenium.webdriver.common.by import By
from iwebshop.test_case.page_obj.backSystem.backHomePage import backhome
from selenium.common.exceptions import NoSuchElementException

class BackSystem(backhome):
    """提供后台系统管理的菜单选择功能：（网站管理：网站设置、主题设置；支付设置：支付方式；
    多平台登录：平台列表；配送管理：配送方式、地区管理、物流公司、快递跟踪；权限管理：管理员、角色、权限资源；系统升级：系统升级）"""
    back_system_wangzhanshezhi = (By.LINK_TEXT, u"网站设置")
    back_system_zhutishezhi = (By.LINK_TEXT, u"主题设置")
    back_system_zhifufangshi = (By.LINK_TEXT, u'支付方式')
    back_system_pingtailiebiao = (By.LINK_TEXT, u'平台列表')
    back_system_peisongfangshi = (By.LINK_TEXT, u'配送方式')
    back_system_kuaidigenzong = (By.LINK_TEXT, u'快递跟踪')
    back_system_diquguanli = (By.LINK_TEXT, u'地区管理')
    back_system_wuliugongsi = (By.LINK_TEXT, u'快递跟踪')
    back_system_guanliyuan = (By.LINK_TEXT, u'管理员')
    back_system_juese = (By.LINK_TEXT, u'角色')
    back_system_quanxianziyuan = (By.LINK_TEXT, u'权限资源')
    back_system_xitongshengji = (By.LINK_TEXT, u'系统升级')

    def click_wangzhanguanli(self):
        '''进入网站管理界面'''
        return self.find_elemet(*self.back_system_wangzhanshezhi).click()

    def click_zhutishezhi(self):
        '''进入主题设置'''
        self.find_elemet(*self.back_system_zhutishezhi).click()

    def click_zhifufangshi(self):
        '''进入支付方式界面'''
        self.find_elemet(*self.back_system_zhifufangshi).click()

    def click_pingtailiebiao(self):
        '''进入平台列表界面'''
        self.find_elemet(*self.back_system_pingtailiebiao).click()

    def click_peisongfangshi(self):
        '''进入配送方式界面'''
        self.find_elemet(*self.back_system_peisongfangshi).click()

    def click_kuaidigenzong(self):
        '''进入快递跟踪界面'''
        self.find_elemet(*self.back_system_kuaidigenzong).click()

class JiBenSheZhi(backhome):
    """
    @网站设置，基本功能：实现基本设置、导航设置、首页幻灯片设置、站点底部设置、购物设置、图片设置、邮箱设置、系统设置功能；
    """
    def input_shangdianName(self, shangpinname):
        """输入商店名字
        @shangpinname : 填写的商店名称"""
        name = (By.NAME, 'name')
        input_name = str(shangpinname)
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_shangdianName_prompt(self):
        """获取商店名称提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[1]/td/label')
        element = self.find_elemet(*name).text
        return element

    def input_shangdiandizhi(self, url):
        """输入商店URL地址
         @URL : 商店的完整URL"""
        name = (By.NAME, 'url')
        input_name = str(url)
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_shangdiandizhi_prompt(self):
        """获取商店URL地址提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[2]/td/label')
        element = self.find_elemet(*name).text
        return element

    def input_shangdianlogo(self, file):
        """输入商店Logo图片
          @file : 商店Logo图片的文件路径"""
        name = (By.NAME, 'logo')
        input_name = file
        self.find_elemet(*name).send_keys(input_name)

    def input_lianxiren(self, turnName):
        """输入联系人
        @turnName : 商店联系人"""
        name = (By.NAME, 'master')
        if isinstance(turnName, unicode):
             input_name = turnName
        else:
            input_name = unicode(turnName, "gbk")
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def input_QQ(self, QQ):
        """输入联系人
        @QQ : 商店QQ"""
        name = (By.NAME, 'qq')
        input_name = str(QQ)
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_QQ_prompt(self):
        """获取商店QQ提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[5]/td/label')
        element = self.find_elemet(*name).text
        return element

    def input_email(self, emails):
        """@emails : 商店email"""
        name = (By.NAME, 'email')
        input_name = str(emails)
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_email_prompt(self):
        """获取商店email提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[6]/td/label')
        element = self.find_elemet(*name).text
        return element

    def input_mobile(self, mobile):
        """@mobile : 商店手机号"""
        name = (By.NAME, 'mobile')
        if type(mobile) == type('strings'):
            input_name = unicode(mobile, "gbk")
        else:
            input_name = mobile
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_mobile_prompt(self):
        """获取手机提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[7]/td/label')
        element = self.find_elemet(*name).text
        return element

    def input_phone(self, phone):
        """@mobile : 商店手机号"""
        name = (By.NAME, 'phone')
        input_name = str(phone)
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_phone_prompt(self):
        """获取固定电话提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[8]/td/label')
        element = self.find_elemet(*name).text
        return element

    def input_jutidizhi(self, address):
        """@address : 商店的具体地址"""
        name = (By.NAME, 'address')
        if type(address) == type('strings'):
            input_name = unicode(address, "gbk")
        else:
            input_name = address
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_jutidizhi_prompt(self):
        """获取具体地址提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[9]/td/label')
        element = self.find_elemet(*name).text
        return element

    def input_huohaoqianzhui(self, shangpinqianzhui):
        """@shangpinqianzhui : 商店的商品货号前缀"""
        name = (By.NAME, 'goods_no_pre')
        if type(shangpinqianzhui) == type('strings'):
            input_name = unicode(shangpinqianzhui, "gbk")
        else:
            input_name = shangpinqianzhui
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_huohaoqianzhui_prompt(self):
        """获取商店商品货号前缀提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[10]/td/label')
        element = self.find_elemet(*name).text
        return element

    def input_titleHouZhui(self, shouyehouzhui):
        """@shouyehouzhui : 首页title后缀"""
        name = (By.NAME, 'index_seo_title')
        if type(shouyehouzhui) == type('strings'):
            input_name = unicode(shouyehouzhui, "gbk")
        else:
            input_name = shouyehouzhui
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_titleHouZhui_prompt(self):
        """获取商店商品货号前缀提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[11]/td/label')
        element = self.find_elemet(*name).text
        return element

    def input_keywords(self, keywords):
        """@keywords : 首页keywords"""
        name = (By.NAME, 'index_seo_keywords')
        input_name = str(keywords)
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_keywords_prompt(self):
        """获取首页keywords提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[12]/td/label')
        element = self.find_elemet(*name).text
        return element

    def input_description(self, description):
        """@description : 首页description"""
        name = (By.NAME, 'index_seo_description')
        input_name = str(description)
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_description_prompt(self):
        """获取首页description提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[1]/table/tbody/tr[13]/td/label')
        element = self.find_elemet(*name).text
        return element

    def click_submit(self):
        """@submit : 保存基本设置"""
        name = (By.CLASS_NAME, 'submit')
        self.find_elemet(*name).click()

    def get_prompt(self):
        """@基本功能：获取保存基本设置提示信息
        @提示语：保存成功、logo图片上传失败；
        """
        name = (By.ID, 'artPlustipscontent')
        self.driver.implicitly_wait(5)
        element = self.find_elemet(*name).text
        return element

    def get_prompt_txt(self):
        """循环获取提示信息，优先获取弹窗提示语，不存在时，获取各个输入框提示语"""
        prompt = ''
        try:
            prompt = self.get_prompt()
        except NoSuchElementException:
            if self.get_shangdianName_prompt() != '':
                prompt = self.get_shangdianName_prompt()
            elif self.get_shangdiandizhi_prompt() != '':
                prompt = self.get_shangdiandizhi_prompt()
            elif self.get_QQ_prompt() != '':
                prompt = self.get_QQ_prompt()
            elif self.get_email_prompt():
                prompt =self.get_email_prompt()
            elif self.get_mobile_prompt() != '':
                prompt = self.get_mobile_prompt()
            elif self.get_phone_prompt() != '':
                prompt = self.get_phone_prompt()
            else:
                prompt = self.get_jutidizhi_prompt()
        return prompt

class DaoHangSheZhi(backhome):
    """@实现导航设置"""
    def get_table_hang(self):
        """获取导航列表行数"""
        elements = self.find_elemets(By.TAG_NAME, 'tr')
        numbers = len(elements)
        return numbers

    def input_daoHangName(self, number, daohangName ):
        """@输入导航名称
        @number:导航名称所在的行数；
        @daohangName:导航名称"""
        name = daohangName
        xpath = '//*[@id="guide_box"]/tbody/tr['+ number + ']/td[1]/input'
        input_name = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*input_name).send_keys(name)
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def get_daoHangName_prompt(self, number):
        """@获取导航名称错误提示
        @number:导航名称所在的行数；"""
        xpath = '//*[@id="guide_box"]/tbody/tr[' + number + ']/td[1]/label'
        label = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            prompt = self.find_elemet(*label).text
            return prompt
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def input_daoHangLink(self, number, daohangLink ):
        """@输入导航链接地址
        @number:导航链接地址所在的行数；
        @daohangLink:导航链接地址"""
        name = daohangLink
        xpath = '//*[@id="guide_box"]/tbody/tr['+ number + ']/td[2]/input'
        input_names = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*input_names).send_keys(name)
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def get_daoHangLink_prompt(self, number):
        """@获取导航地址错误提示
        @number:导航链接地址所在的行数；"""
        xpath = '//*[@id="guide_box"]/tbody/tr[' + number + ']/td[2]/label'
        input_names = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            return self.find_elemet(*input_names).text
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def click_xiangShangYi(self, number):
        """将改行向上移动
        @number:导航链接地址所在的行数；"""
        xpath = '//*[@id="guide_box"]/tbody/tr['+ number + ']/td[3]/img[1]'
        input_names = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*input_names).click()
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def click_xiangXiaYi(self, number):
        """将改行向下移动
        @number:导航链接地址所在的行数；"""
        xpath = '//*[@id="guide_box"]/tbody/tr['+ number + ']/td[3]/img[2]'
        input_names = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*input_names).click()
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def click_delete(self, number):
        """将本行删除
        @number:导航链接地址所在的行数；"""
        xpath = '//*[@id="guide_box"]/tbody/tr['+ number + ']/td[3]/img[3]'
        input_names = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*input_names).click()
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def get_delete_prompt(self):
        """获取删除提示语"""
        xpath = '//*[@id="artPlusConfirmcontent"]'
        element = (By.XPATH, xpath)
        try:
            prompt = self.find_elemet(*element).text
            return prompt
        except NoSuchElementException as msg:
            print u"查找元素异常%s" %msg
            return u"查找元素异常!"

    def click_delete_yes(self):
        """确定删除导航"""
        xpath = '//*[@id="artPlusConfirmyes"]'
        element = (By.XPATH, xpath)
        try:
            self.find_elemet(*element).click()
        except NoSuchElementException as msg:
            print u"查找元素异常%s" %msg

    def click_delete_no(self):
        """取消删除导航"""
        xpath = '//*[@id="artPlusConfirmno"]'
        element = (By.XPATH, xpath)
        try:
            self.find_elemet(*element).click()
        except NoSuchElementException as msg:
            print u"查找元素异常%s" %msg

    def click_tianJiaDaoHang(self):
        """添加导航"""
        input_name = (By.XPATH, '//*[@id="guide_box"]/tfoot/tr/td/button/span')
        self.find_elemet(*input_name).click()

    def click_saveDaoHang(self):
        """保存导航栏配置"""
        input_name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[2]/table/tbody/tr[2]/td/button/span')
        self.find_elemet(*input_name).click()

    def get_save_prompt(self):
        """@基本功能：获取保存导航栏设置提示信息
        @提示语：保存成功；
        """
        name = (By.ID, 'artPlustipscontent')
        self.driver.implicitly_wait(5)
        element = self.find_elemet(*name).text
        return element

class ShouYeHuanDengSheZhi(backhome):
    """@实现首页幻灯设置"""
    def get_table_hang(self):
        """获取首页幻灯设置表行数"""
        elements = self.find_elemets(By.TAG_NAME, 'tr')
        numbers = len(elements)
        return numbers

    def input_huanDengName(self, number, huandengName ):
        """@输入首页幻灯名称
        @number:幻灯片名称所在的行数；
        @daohangName:首页幻灯名称"""
        name = huandengName
        xpath = '//*[@id="slide_box"]/tbody/tr['+ number + ']/td[1]/input'
        input_name = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*input_name).send_keys(name)
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def get_huanDengName_prompt(self, number):
        """@获取首页幻灯名称错误提示
        @number:首页幻灯名称所在的行数；"""
        xpath = '//*[@id="slide_box"]/tbody/tr[' + number + ']/td[1]/label'
        label = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            prompt = self.find_elemet(*label).text
            return prompt
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def input_huanDengLink(self, number, huanDengLink ):
        """@输入首页幻灯片链接地址
        @number:幻灯片链接地址所在的行数；
        @daohangLink:首页幻灯链接地址"""
        name = huanDengLink
        xpath = '//*[@id="slide_box"]/tbody/tr['+ number + ']/td[2]/input'
        input_names = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*input_names).send_keys(name)
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def get_huanDengLink_prompt(self, number):
        """@获取首页幻灯地址错误提示
        @number:导航链接地址所在的行数；"""
        xpath = '//*[@id="slide_box"]/tbody/tr[' + number + ']/td[2]/label'
        input_names = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            return self.find_elemet(*input_names).text
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def input_huanDengTuPian(self, number, file):
        """输入幻灯图片文件地址
          @file : 幻灯图片的文件路径"""
        name = (By.NAME, 'slide_pic[]')
        input_name = file
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*name).send_keys(input_name)
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def click_xiangShangYi(self, number):
        """将改行向上移动
        @number:导航链接地址所在的行数；"""
        xpath = '//*[@id="slide_box"]/tbody/tr['+ number + ']/td[4]/img[1]'
        input_names = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*input_names).click()
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def click_xiangXiaYi(self, number):
        """将改行向下移动
        @number:导航链接地址所在的行数；"""
        xpath = '//*[@id="slide_box"]/tbody/tr['+ number + ']/td[4]/img[2]'
        input_names = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*input_names).click()
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def click_delete(self, number):
        """将本行删除
        @number:导航链接地址所在的行数；"""
        xpath = '//*[@id="slide_box"]/tbody/tr['+ number + ']/td[4]/img[3]'
        input_names = (By.XPATH, xpath)
        zonghangshu = self.get_table_hang()
        if number > zonghangshu:
            self.find_elemet(*input_names).click()
        else:
            raise ValueError(u'输入的行数不存在，请检查！')

    def get_delete_prompt(self):
        """获取删除提示语"""
        xpath = '//*[@id="artPlusConfirmcontent"]'
        element = (By.XPATH, xpath)
        try:
            prompt = self.find_elemet(*element).text
            return prompt
        except NoSuchElementException as msg:
            print u"查找元素异常%s" %msg
            return u"查找元素异常!"

    def click_delete_yes(self):
        """确定删除导航"""
        xpath = '//*[@id="artPlusConfirmyes"]'
        element = (By.XPATH, xpath)
        try:
            self.find_elemet(*element).click()
        except NoSuchElementException as msg:
            print u"查找元素异常%s" %msg

    def click_delete_no(self):
        """取消删除导航"""
        xpath = '//*[@id="artPlusConfirmno"]'
        element = (By.XPATH, xpath)
        try:
            self.find_elemet(*element).click()
        except NoSuchElementException as msg:
            print u"查找元素异常%s"  %msg

    def click_tianJiaHuanDeng(self):
        """添加幻灯"""
        input_name = (By.XPATH, '//*[@id="slide_box"]/tfoot/tr/td/button/span')
        self.find_elemet(*input_name).click()

    def click_saveDaoHang(self):
        """保存首页幻灯配置"""
        input_name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[3]/table/tbody/tr[2]/td/button/span')
        self.find_elemet(*input_name).click()

    def get_save_prompt(self):
        """@基本功能：获取保存首页幻灯设置提示信息
        @提示语：保存成功；
        """
        name = (By.ID, 'artPlustipscontent')
        self.driver.implicitly_wait(5)
        element = self.find_elemet(*name).text
        return element

class ZhanDianDiBuXinXi(backhome):
    """@站点底部信息"""
    def input_xinXi(self, xinxi):
        """@xinxi:输入站点底部信息"""
        name = (By.XPATH, '/html/body')
        input_name = xinxi
        element = self.find_elemet(*name)
        element.clear()
        element.click()
        element.send_keys(input_name)

    def click_baoCunZhanDianDiBuXinXi(self):
        """点击保存站点底部信息"""
        name = (By.CLASS_NAME, 'submit')
        self.find_elemet(*name).click()

    def get_prompt(self):
        """@基本功能：获取保存购物设置提示信息
        @提示语：保存成功；
        """
        name = (By.ID, 'artPlustipscontent')
        self.driver.implicitly_wait(5)
        element = self.find_elemet(*name).text
        return element

class GouWuSheZhi(backhome):
    """@购物设置：设置税率、默认备货时间、团购过期时间"""
    def input_shuiLv(self, shuilv):
        """@shuilv:输入税率，单位：％"""
        name = (By.NAME, 'tax')
        input_name = shuilv
        element = self.find_elemet(*name)
        element.clear()
        element.click()
        element.send_keys(input_name)

    def get_shuiLv_prompt(self):
        """获取税率提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[5]/table/tbody/tr[1]/td/label')
        element = self.find_elemet(*name).txt
        return element

    def input_moRenBeiHuoShiJian(self, beihuoTime):
        """@beihuoTime:输入默认备货时间，单位：天"""
        name = (By.NAME, 'name')
        input_name = beihuoTime
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_moRenBeiHuoShiJian_prompt(self):
        """获取默认备货时间提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[5]/table/tbody/tr[2]/td/label')
        element = self.find_elemet(*name).txt
        return element

    def input_tuanGouGuoQiShiJian(self, guoqiTinme):
        """@guoqiTime: 输入团购过期时间，单位：分钟"""
        name = (By.NAME, 'name')
        input_name = str(guoqiTinme)
        self.find_elemet(*name).clear()
        self.find_elemet(*name).click()
        self.find_elemet(*name).send_keys(input_name)

    def get_tuanGouGuoQiShiJian_prompt(self):
        """获取团购过期时间提示语"""
        name = (By.XPATH, '//*[@id="admin_right"]/div[2]/div/form[5]/table/tbody/tr[2]/td/label')
        element = self.find_elemet(*name).txt
        return element

    def click_baoCunGuoWuSheZhi(self):
        """点击保存购物设置"""
        name = (By.NAME, 'name')
        self.find_elemet(*name).click()

    def get_prompt(self):
        """@基本功能：获取保存购物设置提示信息
        @提示语：保存成功；
        """
        name = (By.ID, 'artPlustipscontent')
        self.driver.implicitly_wait(5)
        element = self.find_elemet(*name).text
        return element



if __name__ == '__main__':
    from selenium import webdriver
    from iwebshop.iwebshop.test_case.models.function import insert_img
    driver = webdriver.Chrome()
    a=BackSystem(driver, "http://localhost/iwebshop/index.php?controller=systemadmin&action=index")
    a.adminLogin()
    # a.click_backhome_system()
    # driver.implicitly_wait(5)
    a.click_wangzhanguanli()
    b = JiBenSheZhi(a.driver)
    b.input_shangdianName('iwebshop')
    b.input_shangdiandizhi('http://www.baidu.com')
    files = 'C:\\25941409.jpg'
    b.input_shangdianlogo(files)
    b.input_lianxiren(u'张三')
    b.input_QQ('53179275')
    b.input_email('531462465@qq.com')
    b.input_mobile('18701201222')
    b.input_phone('18720130221')
    b.input_jutidizhi('88888')
    b.input_huohaoqianzhui('huohao')
    b.input_titleqianzhui('ccc')
    # b.input_keywords('abc')
    # b.input_description('jingkkk')
    b.click_submit()
    if b.get_prompt() == u'保存成功':
        print u'保存基本设置成功！'
    else:
        print u"保存基本设置失败！"
    insert_img(b.driver, u"全部会员删除成功.jpg")
    driver.quit()