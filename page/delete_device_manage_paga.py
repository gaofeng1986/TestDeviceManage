#coding = utf-8
from dddd.base_page.basepage import BasePage


class DeleteDeviceManagePage(BasePage):

    # 点击设备管理菜单
    def click_device_manage_menu(self):
        self.click_ele("xpath=>//a[text()='设备管理']")

    # 从主iframe 跳转 列表iframe
    def switch_main_to_list(self):
        # self.switch_outin_iframe("name=>iframe_a")
        self.driver.switch_to.frame('iframe_a')

        # 点击删除按钮
    def click_delete_btn(self,para):
        ele_xpath = 'xpath=>//div[text()="{}"]/parent::td/following-sibling::td[3]/div/a[text()="删除"]'.format(para)
        self.click_ele(ele_xpath)

    # 点击取消按钮
    def click_quxiao_btn(self):
        self.click_ele('xpath=>//span[text()="取消"]')

    # 点击二次确认
    def click_second_queding(self):
        self.click_ele('xpath=>//span[text()="确定"]')

