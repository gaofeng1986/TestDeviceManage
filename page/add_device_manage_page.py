# coding = utf-8
# 页面对象模型之页面封装
from dddd.base_page.basepage import BasePage


class AddDeviceManagePage(BasePage):

    def click_device_manage_menu(self):
        self.click_ele("xpath=>//a[text()='设备管理']")

    def switch_main_to_list(self):
        self.driver.switch_to.frame('iframe_a')              # 进入iframe 模块

    def click_add_btn(self):
        self.click_ele("xpath=>//input[@value='新增']")
        # self.driver.find_element_by_xpath("//input[@value='新增']").click()     # 定位新增按钮元素，并点击

    def switch_list_to_winiframe(self):
        self.driver.switch_to.frame('showMyWindowId')         # 从外层列表iframe进入到里层新增弹窗的iframe模块

    def input_number(self,para):  # 输入5位编号
        self.input_bianhao('xpath=>//*[@id="_easyui_textbox_input1"]',para)
        # self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').send_keys(para)     # 定位新增弹窗中的编号输入框元素，并输入编号

    def input_name(self,para):
        self.input_bianhao('xpath=>//*[@id="_easyui_textbox_input2"]',para)
        # self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input2"]').send_keys(para)      # 定位新增弹窗中的名称输入框元素，并输入名称

    def click_queding(self):
        self.click_ele("xpath=>//a[text()='确定']")
        # self.driver.find_element_by_xpath('//a[text()="确定"]').click()        # 定位新增弹窗中的确定按钮，并点击

    def quit_iframe_father(self):
        self.driver.switch_to.parent_frame()           # 退出新增弹窗的iframe,退值父级

    def input_number_6(self,para):     # 输入6位编号
        self.input_bianhao('xpath=>//*[@id="_easyui_textbox_input1"]',para)
        # self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').send_keys(para)

    def input_number_4(self,para):     # 输入4位编号
        self.input_bianhao('xpath=>//*[@id="_easyui_textbox_input1"]',para)
        # self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').send_keys(para)

    # def buhuo_except(self):  # 定位设备列表新增的设备编号，找不到
    #     self.assertIsNotNone(self.driver.find_element_by_xpath("//div[text()='编号只能为5个字符!']"))