import requests
import sys
#sys.path.append("F:\ProgramFiles\jenkins_python\jenkins_test")
import os,sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("F:\ProgramFiles\Lib\site-packages")
import unittest
from HTMLTestRunner import HTMLTestRunner
from util.send_email import Send_email
class NewCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    def test_01(self):
        # aa='123'
        # self.assertEqual(aa,'123',msg="相等")
       # print("test_01 going......")
        pass


    def test_02(self):
        # aa = '123'
        #
        # print("test_02 going......")
        # self.assertEqual(aa, '123', msg="不相等")
        pass

  
if __name__=='__main__':
    sendEmail=Send_email()
    ReportPath='../report/TestReport2.html'
    fp=open(ReportPath,"wb")
    suite=unittest.TestSuite()
    suite.addTest(NewCase("test_01"))
    suite.addTest(NewCase("test_02"))
    runner=HTMLTestRunner(stream=fp,title=u"第一个测试报告")
    runner.run(suite)
    fp.close()
    user_list1 = ['yanshunhua163@163.com']
    sub = '接口测试报告'
    content = "这是我们的一封测试邮件，测试完成"
    file_names = ["../report/TestReport2.html"]
    sendEmail.send_mail(user_list1,sub,content,file_names)

