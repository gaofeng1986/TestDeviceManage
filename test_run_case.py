# coding = utf-8

import unittest
import time

from HTMLTestRunner_cn import HTMLTestRunner

if __name__ == '__main__':


    # test_dir = "./test_case"
    # discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_case.py')
    # print(discover)
    # runner = unittest.TextTestRunner()    #实例化一个执行对象
    # runner.run(discover)     # 利用run对象的run方法执行测试用例及测试套件集合

    # 运行全部用例，生成html测试报告
    test_dir = './test_case'          #执行用例 路径
    test_report_dir = './report'      # 报告路径
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')         # 生成时间戳
    filename = test_report_dir + '\\' + now + 'result.html'    # 生成报告文件
    fp = open(filename,'wb')            # 以二进制可写方式打开文件
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_case.py')        # 执行所有 _case.py的文件
    # title：标题；     description：描述      stream：报告文件     verbosity：详细程度      retry：重试次数    save_last_try：保存最后一次重试
    runner = HTMLTestRunner(title="排队管理后台测试报告", description="我的文档", stream=fp, verbosity=2, retry=2, save_last_try=True)
    runner.run(discover)
    fp.close()      # 必须加上关闭，否则生成不了报告

