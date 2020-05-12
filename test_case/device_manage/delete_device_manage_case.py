#coding= utf-8
import unittest
from time import sleep

from dddd.commen.get_browser import get_browser
from numpy import random

from dddd.commen.db_opterate.device_data import *
from dddd.commen.sys_config import liulanqi_type, web_url, time_out
from dddd.page.delete_device_manage_paga import DeleteDeviceManagePage


class DeleteDeviceManage(unittest.TestCase):
    '''
    删除设备管理
    '''

    @classmethod
    def setUpClass(cls):
        cls.driver = get_browser(liulanqi_type)  # 实例化谷歌浏览器，并打开浏览器
        cls.driver.maximize_window()  # 浏览器窗口最大化
        cls.driver.implicitly_wait(time_out)  # 添加隐式等待
        cls.driver.get(web_url)  # 打开测试项目
        cls.delete_device_manage_page = DeleteDeviceManagePage(cls.driver)

    def setUp(self):

        self.i = random.randint(10000,99999)
        add_device(self.i,"gfgf")

    def test_01_delete_device_manage_success(self):
        '''成功删除设备'''

        self.delete_device_manage_page.click_device_manage_menu()       #定位设备管理按钮，并单击
        # self.device.find_element_by_xpath('//a[text()="设备管理"]')

        self.delete_device_manage_page.switch_main_to_list()          # 从主页iframe 跳转列表iframe
        # self.device.switch_to_frame('iframe_a')

        print(self.i)
        self.delete_device_manage_page.click_delete_btn(self.i)    #定位删除按钮并点击
        # self.device.find_element_by_xpath('//div[text()="96538"]/parent::td/following-sibling::td[3]/div/a[text()="删除"]').click()

        self.delete_device_manage_page.click_second_queding()      #点击二次确认
        # self.device.find_element_by_xpath('//span[text()="确定"]').click()

        sleep(5)    # 强制等待，因为刚删除完数据提示框消失前还能查到被删数据，会报错，因此需要等会儿再断言
        xpath = "xpath=>//div[text()='{}']".format(self.i)      # 断言设备数据被删除
        self.assertFalse(self.delete_device_manage_page.element_is_exists(xpath))
        # self.assertFalse(self.device.find_element_by_xpath('//div[text()="96538"]'))

    def test_02_delete_device_manage_fail(self):
        '''删除设备失败'''

        self.delete_device_manage_page.click_device_manage_menu()  # 定位设备管理按钮，并单击
        # self.device.find_element_by_xpath('//a[text()="设备管理"]')

        self.delete_device_manage_page.switch_main_to_list()  # 从主页iframe 跳转列表iframe
        # self.device.switch_to_frame('iframe_a')

        print(self.i)
        self.delete_device_manage_page.click_delete_btn(self.i)  # 定位删除按钮并点击
        # self.device.find_element_by_xpath('//div[text()="96538"]/parent::td/following-sibling::td[3]/div/a[text()="删除"]').click()

        self.delete_device_manage_page.click_quxiao_btn()  # 点击取消按钮
        # self.device.find_element_by_xpath('//span[text()="取消"]').click()

        # 断言，数据是否被删除
        xpath = "xpath=>//div[text()='{}']".format(self.i)
        self.assertTrue(self.delete_device_manage_page.element_is_exists(xpath))
        # self.assertFalse(self.device.find_element_by_xpath('//div[text()="96538"]'))



    def tearDown(self):
        delete_device(self.i)    # 每个用例执行后删除增加的数据
        self.delete_device_manage_page.switch_main_iframe()     #每个用例执行完后跳出主iframe
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()     # 关闭浏览器
