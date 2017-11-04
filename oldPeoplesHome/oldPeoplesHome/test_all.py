# -*- coding: utf-8 -*-
import sys
sys.path.append('D:\\projectTestCase')
import time, unittest
from iwebshop.test_case.models.sendemil import send_mail
from HTMLTestRunner import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    test_dir = './test_case/'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    # 定义报告存放路径
    filename = './report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"电商前台系统测试报告", description=u"测试用例执行情况")
    runner.run(discover)
    fp.close()
    send_mail(["531792735@qq.com"], u"电商前台系统测试报告", filename)

if __name__ == '__main__':
    main()