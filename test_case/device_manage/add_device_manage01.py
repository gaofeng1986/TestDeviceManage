# coding=utf-8
# 导包
from dddd.commen.get_browser import get_browser
from dddd.commen.sys_config import web_url, time_out, liulanqi_type
from numpy import random


class AddDeviceManage:    # 定义 新增设备管理 基类
    '''新增设备管理'''
    def add_device_manage_succes(self):   # 定义函数，验证添加设备时，输入5位数字时，可以添加成功
        self.driver = get_browser(liulanqi_type)  # 实例化谷歌浏览器，并打开浏览器
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_out)  # 添加全局隐式等待
        self.driver.get(web_url)  # 打开测试项目
        self.driver.find_element_by_xpath("//a[text()='设备管理']").click()    # 定位设备管理按钮元素，并点击
        self.driver.switch_to.frame('iframe_a')              # 进入iframe 模块
        self.driver.find_element_by_xpath("//input[@value='新增']").click()     # 定位新增按钮元素，并点击
        self.driver.switch_to.frame('showMyWindowId')         # 从外层列表iframe进入到里层新增弹窗的iframe模块
        i = random.randint(10000,99999)             #  参数化一个变量，使用 random 随机生成一个 5 位数
        self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').send_keys(i)     # 定位新增弹窗中的编号输入框元素，并输入编号
        self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input2"]').send_keys('gfgf')      # 定位新增弹窗中的名称输入框元素，并输入名称
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()        # 定位新增弹窗中的确定按钮，并点击
        self.driver.switch_to.parent_frame()           # 退出新增弹窗的iframe,退值父级
        try:           # 捕获异常
            self.driver.find_element_by_xpath("//div[text() ='{}']".format(i))                # 定位设备列表页面新增的设备编号
            print('设备添加成功')
        except:
            print('设备添加失败')
        self.driver.quit()           # 关闭浏览器

    def add_device_manage_fail_001(self):       # 定义函数， 验证添加设备时编号大于5位时，不能添加成功
        self.driver = get_browser(liulanqi_type)  # 实例化谷歌浏览器，并打开浏览器
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_out)  # 添加全局隐式等待
        self.driver.get(web_url)  # 打开测试项目
        self.driver.find_element_by_xpath("//a[text()='设备管理']").click()           # 定位设备管理按钮元素，并点击
        self.driver.switch_to.frame('iframe_a')            # 进入iframe 模块
        self.driver.find_element_by_xpath("//input[@value='新增']").click()            # 定位新增按钮元素，并点击
        self.driver.switch_to.frame('showMyWindowId')            # 从外层列表iframe进入到里层新增弹窗的iframe模块
        self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').send_keys('112251')          # 定位新增弹窗中的编号输入框元素，并输入编号
        self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input2"]').send_keys('gfgf')           # 定位新增弹窗中的名称输入框元素，并输入名称
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()           # 定位新增弹窗中的确定按钮，并点击
        try:
            self.driver.find_element_by_xpath("//div[text()='编号只能为5个字符!']")              # 定位设备列表页面新增的设备编号
            print('验证编号大于5位时，不能添加')
        except:
            print('验证失败')
        self.driver.quit()           # 关闭浏览器

    def add_device_manage_fail_002(self):    # 定义函数，验证添加设备管理时，输入4位数字时，不能添加成功
        self.driver = get_browser(liulanqi_type)  # 实例化谷歌浏览器，并打开浏览器
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_out)  # 添加全局隐式等待
        self.driver.get(web_url)  # 打开测试项目
        self.driver.find_element_by_xpath("//a[text()='设备管理']").click()          # 定位设备管理按钮元素，并点击
        self.driver.switch_to.frame('iframe_a')          # 进入iframe 模块
        self.driver.find_element_by_xpath("//input[@value='新增']").click()          # 定位新增按钮元素，并点击
        self.driver.switch_to.frame('showMyWindowId')          # 从外层列表iframe进入到里层新增弹窗的iframe模块
        self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').send_keys('1251')          # 定位新增弹窗中的编号输入框元素，并输入编号
        self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input2"]').send_keys('gfgf')          # 定位新增弹窗中的名称输入框元素，并输入名称
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()           # 定位新增弹窗中的确定按钮，并点击
        try:          # 捕获异常
            self.driver.find_element_by_xpath("//div[text()='编号只能为5个字符!']")               # 定位设备列表页面新增的设备编号
            print('验证编号小于5位时，不能添加')
        except:
            print('验证失败')
        self.driver.quit()  # 关闭浏览器

add_device_manage = AddDeviceManage()              # 创建类的实例
add_device_manage.add_device_manage_succes()       # 调用验证添加设备时，输入5位数字时，可以添加成功
# add_device_manage.add_device_manage_fail_001()     # 调用验证添加设备时编号大于5位时，不能添加成功
# add_device_manage.add_device_manage_fail_002()     # 调用验证添加设备管理时，输入4位数字时，不能添加成功