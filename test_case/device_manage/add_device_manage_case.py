# coding=utf-8
# 导包
import unittest

from dddd.commen.db_opterate.device_data import add_device
from dddd.commen.get_browser import get_browser
from dddd.commen.sys_config import liulanqi_type
from dddd.commen.sys_config import web_url, time_out
from dddd.page.add_device_manage_page import AddDeviceManagePage
from numpy import random


class AddDeviceManage(unittest.TestCase):    # 定义 新增设备管理 基类
    '''新增设备管理'''
    # @classmethod
    # def setUpClass(cls):
    @classmethod
    def setUpClass(cls):      # 每个用例执行前执行一次
        cls.driver = get_browser(liulanqi_type)          # 实例化谷歌浏览器，并打开浏览器
        cls.driver.maximize_window()                   #浏览器最大化
        cls.driver.implicitly_wait(time_out)           # 添加全局隐式等待
        cls.driver.get(web_url)           # 打开测试项目
        cls.add_device_manage_page = AddDeviceManagePage(cls.driver)
        add_device("77676","gfgf")

    def setUp(self):
        pass

    def test_001_add_device_manage_success_01(self):   # 定义函数，验证添加设备时，输入5位数字时，可以添加成功
        '''新增设备管理成功'''
        #第一步，点击设备管理菜单
        self.add_device_manage_page.click_device_manage_menu()
        # 第二步，进入iframe
        self.add_device_manage_page.switch_main_to_list()
        # 第三步，点击新增按钮
        self.add_device_manage_page.click_add_btn()
        #第四步，从列表ifram跳转弹窗iframe
        self.add_device_manage_page.switch_list_to_winiframe()
        # 第五步，给编号输入框输值,5 为数字    参数化一个变量，使用 random 随机生成一个 5 位数
        i = random.randint(10000,99999)
        self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').send_keys(i)
        # 第六步，给名称输入框输值
        self.add_device_manage_page.input_name("gfgf")
        # 第七步，点击确定
        self.add_device_manage_page.click_queding()
        # 第八步，退iframe至父级
        self.add_device_manage_page.quit_iframe_father()
        # 第九步，验证实际结果与预期结果
        self.assertIsNotNone(self.driver.find_element_by_xpath("//div[text() ='{}']".format(i)))   # 捕获异常  定位设备列表页面新增的设备编号
        # self.assertIsNotNone(self.driver.find_element_by_xpath("//div[text()='编号只能为5个字符!']"))

    def test_002_add_device_manage_fail_02(self):       # 定义函数， 验证添加设备时编号大于5位时，不能添加成功
        '''新增设备管理失败，设备编号6位'''
        # 第一步，点击设备管理菜单
        self.add_device_manage_page.click_device_manage_menu()
        #  第二步进入iframe
        self.add_device_manage_page.switch_main_to_list()
        # 第三步 点击新增按钮
        self.add_device_manage_page.click_add_btn()
        # 第四步，从列表ifram跳转弹窗iframe
        self.add_device_manage_page.switch_list_to_winiframe()
        # 第五步，给编号输入框输值,6 为数字   参数化一个变量，使用 random 随机生成一个 6 位数
        i = random.randint(100000,999999)
        self.add_device_manage_page.input_number_6(i)
        #第六步，给名称输入框输入值
        self.add_device_manage_page.input_name("gfgfblbl")
        # 第七步，点击弹窗确定
        self.add_device_manage_page.click_queding()
        # 第八步，验证实际结果与预期结果，添加6位编号的设备管理失败
        # self.add_device_manage_page.buhuo_except()
        self.assertIsNotNone(self.driver.find_element_by_xpath("//div[text()='编号只能为5个字符!']"))   # 定位设备列表页面新增的设备编号,不存在，

    def test_003_add_device_manage_fail_03(self):    # 定义函数，验证添加设备管理时，输入4位数字时，不能添加成功
        '''新增设备管理失败，设备编号6位'''
        # 第一步，点击设备管理
        self.add_device_manage_page.click_device_manage_menu()
        # 第二步，进入iframe
        self.add_device_manage_page.switch_main_to_list()
        # 第三步，点击新增按钮
        self.add_device_manage_page.click_add_btn()
        # 第四步，从列表ifram跳转弹窗iframe
        self.add_device_manage_page.switch_list_to_winiframe()          #
        # 第五步，给编号输入框输值,4 为数字    参数化一个变量，使用 random 随机生成一个 6 位数
        i = random.randint(1000,9999)      #
        self.add_device_manage_page.input_number_4(i)
        # 第六步，给名称输入框输入值
        self.add_device_manage_page.input_name("gfgf")
        # 第七步，点击弹窗中的确定
        self.add_device_manage_page.click_queding()
        # 第八步，验证实际结果与预期结果，添加4位编号的设备管理失败
        # self.add_device_manage_page.buhuo_except()   # 定位设备列表页面新增的设备编号
        self.assertIsNotNone(self.driver.find_element_by_xpath("//div[text()='编号只能为5个字符!']"))    # 定位设备列表页面新增的设备编号,不存在，


    def test_004_add_device_manage_fail_04(self):   # 定义添加设备管理时名称必填项为空
        '''新增设备管理失败，名称为空'''
        # 第一步，点击设备管理菜单
        self.add_device_manage_page.click_device_manage_menu()
        # 第二步，进入iframe
        self.add_device_manage_page.switch_main_to_list()
        # 第三步，点击新增按钮
        self.add_device_manage_page.click_add_btn()
        # 第四步，从列表iframe跳转弹窗iframe
        self.add_device_manage_page.switch_list_to_winiframe()
        # 第五步，给输入框输入5位数字
        i = random.randint(10000,99999)
        self.add_device_manage_page.input_number(i)
        # 第六步，点击确定按钮
        self.add_device_manage_page.click_queding()
        # 第七步，验证实际结果与预期结果
        self.assertIsNotNone(self.driver.find_element_by_xpath('//div[text()="姓名不能为空!"]'))

    def test_005_add_device_manage_fail_05(self):   # 定义添加重复设备管理
        '''新增重复设备管理，添加失败'''

        # 第一步，点击设备管理菜单
        self.add_device_manage_page.click_device_manage_menu()
        # 第二步，进入iframe
        self.add_device_manage_page.switch_main_to_list()
        # 第三步，点击新增按钮
        self.add_device_manage_page.click_add_btn()
        # 第四步，从列表iframe跳转弹窗iframe
        self.add_device_manage_page.switch_list_to_winiframe()
        # 第五步，给输入框输入5位数字
        self.add_device_manage_page.input_number("77676")
        # 第六步，给名称输入框输入值
        self.add_device_manage_page.input_name("gfgf")  # 定位新增弹窗中的名称输入框元素，并输入名称
        # 第七步，点击确定按钮
        self.add_device_manage_page.click_queding()
        # 第八步，验证实际结果与预期结果
        self.assertIsNotNone(self.driver.find_element_by_xpath('//div[text()="当前设备编号已经存在，请重新输入！"]'))

    def tearDown(self):
        self.add_device_manage_page.switch_main_iframe()      # 每个用例执行完，iframe跳转至最外层

    @classmethod
    def tearDownClass(cls):  # 每个用例执行后执行一次
        cls.driver.quit()  # 关闭浏览器


# add_device_manage = AddDeviceManage()              # 创建类的实例
# add_device_manage.add_device_manage_success()       # 调用验证添加设备时，输入5位数字时，可以添加成功
# add_device_manage.add_device_manage_fail_001()     # 调用验证添加设备时编号大于5位时，不能添加成功
# add_device_manage.add_device_manage_fail_002()     # 调用验证添加设备管理时，输入4位数字时，不能添加成功
if __name__ == '__main__':
    unittest.main()