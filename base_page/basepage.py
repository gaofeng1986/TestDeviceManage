# coding = utf-8

# 封装公共的功能，定位元素、点击事件、输入框输入值、iframe跳转等等
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    # 定位页面元素
    def find_element(self,selector):
        selector = selector.strip(" ")
        strs = selector.split("=>")
        if strs[0] == "id":
            return self.driver.find_element_by_id(strs[1])
        elif strs[0] == "name":
            return self.driver.find_element_by_name(strs[1])
        elif strs[0] == "class":
            return self.driver.find_element_by_class(strs[1])
        elif strs[0] == "xpath":
            return self.driver.find_element_by_xpath(strs[1])
        else:
            print("定位方式不正确，请输入正确的定位方式")

    #点击页面元素
    def click_ele(self,selector):
        self.find_element(selector).click()

    #给输入框输入值
    def input_bianhao(self,selector,para):
        num = self.find_element(selector)
        num.clear()
        num.send_keys(para)

    # 跳转iframe--从外往里跳
    def switch_outin_iframe(self,selector):
        ele = self.find_element(selector)
        self.driver.switch_to.iframa(ele)

    # 跳转iframe--从里往外跳
    def switch_inout_iframe(self):
        self.driver.switch_to.iframa()

    # 跳转iframe--主文档
    def switch_main_iframe(self):
        self.driver.switch_to.default_content()

    #判断元素是否存在
    def element_is_exists(self,selector):
        try:
            self.find_element(selector)
            return True
        except:
            return False


if __name__ == "__main__":
    pass