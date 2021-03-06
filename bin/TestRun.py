#coding=utf-8

import unittest
# import HTMLTestReportYIF
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.config import *
from utils.email_error import email
import HTMLTestRunner
import shutil

def allInterfaceTests():
    print("路径信息：",os.path.join("./", 'tests', 'pqm_interface'))
    suite =unittest.TestLoader().discover(
        start_dir=os.path.join(TESTCAST_PATH, 'pqm_interface'),
        pattern='test_all*.py',
        top_level_dir=None
    )

    return suite


def allUiTests():
    suite =unittest.TestLoader().discover(
        start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),r'tests'),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite

def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def runInterface():
    #move_report()  # 把报告目录移动到report文件夹
    fp = os.path.join(REPORT_PATH,getNowTime()+'testReport.html')
    print(fp)
    '''
    HTMLTestRunner.HTMLTestRunner(
        stream=open(fp,'wb'),
        title='自动化测试报告',
        description='自动化测试报告详细信息').run((allInterfaceTests()))'''
    HTMLTestRunner.HTMLTestRunner(
        stream=open(fp, 'wb'),
        title='自动化测试报告',
        description='自动化测试报告详细信息').run((allInterfaceTests()))
    email(fp,"zhouyifu@yunexpress.com")
# def runUi():
#     fp = os.path.join(REPORT_PATH,getNowTime()+'testReport.html')
#     HTMLTestRunner.HTMLTestRunner(
#         stream=open(fp,'wb'),
#         title='自动化测试报告',
#         description='自动化测试报告详细信息').run((allUiTests()))
def move_report():
    files=os.listdir(REPORT_JENKINS_PATH)
    #print(files)
    for file in files:
        shutil.move(os.path.join(REPORT_JENKINS_PATH,file),REPORT_PATH)
if __name__ == '__main__':
    runInterface()
    #move_report()
    #print("路径信息：", os.path.join("./", 'tests', 'pqm_interface'))
    #print(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests', 'pqm_interface')))

