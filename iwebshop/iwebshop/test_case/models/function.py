# coding=utf-8
from selenium import webdriver
import os
import time
# 截图函数
def insert_img(driver, file_name="Result.jpg"):
    """实现截图功能，需传入：截图保存名称（默认命名为Result.jpg）;截图保存路径为："""
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 当前脚本运行的根目录
    base_dir = str(base_dir)  # 转译成字符串
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    file_name = now + " " + file_name
    file_path = base + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)  # 截图获取当前全部页面，并保存在file_path路径下命名为：file_name


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://localhost/iwebshop")
    insert_img(driver, "iwebshop.jpg")
    driver.quit()
