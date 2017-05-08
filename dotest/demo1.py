#coding=utf-8

import unittest
from selenium.common.exceptions import WebDriverException
import common.readConfig as readConfig
import common.init_phone as init_phone
from appium import webdriver
import common.Log as Log
from urllib2 import URLError
import os
from common.AppiumServer import AppiumServer

readConfigLocal=readConfig.ReadConfig()
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class Demo1(unittest.TestCase):

    # 初始化工作
    def setUp(self):
        #AppiumServer().run_server()
        self.case_name=1
        self.Begin=1
        self.CheckPoint=1
        self.End=1
        self.case_no=1
        print 'begin test'

    def test_demo(self):
        self.assertEqual("2", "2", "test pass")
        print 'kai shi lalalalalallalal'


    def tearDown(self):
        print 'end test'



if __name__=='__main__':
    unittest.main()
