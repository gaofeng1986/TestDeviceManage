# coding = utf-8
# 页面对象模型之页面封装
import unittest

class EditDeviceManagePage(unittest.TestCase):

    def __init__(self,driver):
        self.driver=driver

    def click_device_amnage_menu01(self):
        self.driver.find_element_by_xpath("//a[text()='设备管理']").click()

    def switch_main_to_list(self):
        self.driver.switch_to.frame('iframe_a')              # 进入iframe 模块

    def click_edit_btn(self,apra):
        ele_xpath = '//div[text()="{}"]/parent::td/following-sibling::td[3]/div/a[text()="编辑"]'.format(apra)
        self.driver.find_element_by_xpath(ele_xpath).click()    # 定位编辑按钮元素，并点击

    def switch_list_to_winiframe(self):
        self.driver.switch_to.frame('showMyWindowId')         # 从外层列表iframe进入到里层新增弹窗的iframe模块

    def input_name(self,para):
        ele = self.driver.find_element_by_id('_easyui_textbox_input2')
        ele.clear()
        ele.send_keys(para)

    def click_queding(self):
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()        # 定位新增弹窗中的确定按钮，并点击

    def quit_iframe_father(self):
        self.driver.switch_to.parent_frame()           # 退出新增弹窗的iframe,退值父级

    def update_name_after(self,para):
        self.driver.find_element_by_xpath(para)
