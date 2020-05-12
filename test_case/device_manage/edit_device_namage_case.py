# coding=utf-8
import unittest

from dddd.commen.db_opterate.device_data import add_device, delete_device
from dddd.commen.get_browser import get_browser
from dddd.commen.sys_config import liulanqi_type, time_out, web_url
from dddd.page.edit_device_manage_page import EditDeviceManagePage


class EditDeviceManage(unittest.TestCase):
    '''
    编辑设备管理
    '''
    def setUp(self):
        self.driver = get_browser(liulanqi_type)    # 实例化浏览器，并打开浏览器
        # 窗口最大化
        self.driver.maximize_window()
        # 隐式等待m
        self.driver.implicitly_wait(time_out)
        # 输入测试地址
        self.driver.get(web_url)
        self.edit_device_manage_page = EditDeviceManagePage(self.driver)
        add_device("55555","gfgf")

    def test_edit_device_manage(self):  # 定义函数，编辑设备管理
        '''编辑设备管理'''

        # 第一步，点击设备管理菜单
        self.edit_device_manage_page.click_device_amnage_menu01()

        # 第二步，进入iframe
        self.edit_device_manage_page.switch_main_to_list()

        # 第三步，点击编辑按钮
        self.edit_device_manage_page.click_edit_btn("55555")

        # 第四步，从列表iframe 跳至弹窗iframe
        self.edit_device_manage_page.switch_list_to_winiframe()

        # 第五步，先清空名称输入框，再给名称输入框输入新值
        self.edit_device_manage_page.input_name("gfgfblbl")

        # 第六步，点击确定按钮
        self.edit_device_manage_page.click_queding()

        # 第七步，退出iframe至父级
        self.edit_device_manage_page.quit_iframe_father()

        # 第八步，定位修改后的名称元素
        self.driver.find_element_by_xpath('//div[text()="gfgfblbl"]')


    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()
        delete_device("55555")
