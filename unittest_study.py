# coding = utf-8

import unittest


class AddDevice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有用例执行前只执行一次")


    def setUp(self):
        print("\n每个用例执行前执行一次 ")
    def tearDown(self):
        print("每个用例执行后执行一次")

    def test_01(self):
        a = 1+1
        print("我是01用例")
        self.assertEqual(2,a)

    def test_02(self):
        a = 1*9
        print("我是02用例")
        self.assertEqual(8,a)

    def test_03(self):
        print("我是03用例")

    def test_04(self):
        b =1/0
        print("我是第四个用例")
        self.assertEqual(0,b)
    def tearDown(self):
        print("每个用例执行后执行一次")
    @classmethod
    def tearDownClass(cls):
        print("所有用例执行后只执行一次")

if __name__ == '__main__':
    #第一种方法
    # unittest.main()

    # 第二种方法，只执行其中几个用例
    # suit = unittest.TestSuite()     # 实例化一个测试套件及测试计划
    # suit.addTest(AddDevice("test_03"))     # 给测试计划添加测试用例
    # suit.addTest(AddDevice("test_01"))     # 给测试计划添加测试用例
    # # suit.addTest(AddDeviceManage("test_001_add_device_manage_success"))
    # runner = unittest.TextTestRunner()      # 实例化一个执行对象
    # runner.run(suit)                        # 利用run对象的run方法执行测试用例及测试套件集合

    # 第三种方法
    test.dir = './'
    discover = unittest.defaultTestLoader.discover(test.dir,pattern='*_case.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)