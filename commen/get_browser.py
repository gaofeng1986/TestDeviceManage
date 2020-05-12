
#coding=utf-8

# 定义浏览器方法
from selenium import webdriver
def get_browser(browser_type):
    browser = ''
    if browser_type == 'chrome':
        browser = webdriver.Chrome()
    elif browser_type == 'firefox':
        browser = webdriver.Firefox()
    elif browser_type == 'ie':
        browser = webdriver.Ie()
    else:
        print('对不起！您输入的浏览器暂不支持！')
    return  browser