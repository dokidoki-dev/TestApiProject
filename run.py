import unittest
import os
import libs.HTMLTestRunner3 as HTMLTestRunner
import time


if __name__ == '__main__':
    # 用例文件路径
    case_path = os.path.join(os.path.dirname(os.path.abspath(__file__))) + "\\testcase"
    # 报告存放路径
    report_path = case_path + "\\reports\\"
    # 调试时，执行测试套件，需要生成测试报告需要注释掉此处
    # runner = unittest.TextTestRunner(verbosity=2)
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 2、html报告文件路径
    report_abspath = os.path.join(report_path, "result_" + now + ".html")
    # 3、打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'接口自动化测试报告,测试结果如下：', description=u'用例执行情况：')
    # 执行测试用例
    runner.run(discover)
    fp.close()
