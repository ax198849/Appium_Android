from selenium.common.exceptions import WebDriverException
import readConfig as readConfig
import init_phone
from appium import webdriver
from urllib2 import URLError
import os
import threading

readConfigLocal=readConfig.ReadConfig()
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class MyDriver:

    def __init__(self):
        #self.mutex=threading.Lock()
        self.driver=None
        self.myInit=init_phone.Getphoneinfo()
        self.platformName=readConfigLocal.getConfigValue('platformName')
        self.platformVersion=readConfigLocal.getConfigValue('platformVersion')
        self.appPackage=readConfigLocal.getConfigValue('appPackage')
        self.appActivity=readConfigLocal.getConfigValue('appActivity')
        self.deviceName=self.myInit.get_phone_name()
        self.app=PATH('//Users/alex/Downloads//KooEyes_0.4.2.apk')
        self.baseurl=readConfigLocal.getConfigValue('baseUrl')
        self.desired_caps={"platformName":self.platformName,"platformVersion":self.platformVersion,"app":self.app,"deviceName":self.deviceName}

    def get_driver(self):
        try:
            if self.driver is None:
                 #self.mutex.acquire()
                 if self.driver is None:
                   try:
                     self.driver=webdriver.Remote(self.baseurl,self.desired_caps)
                   except URLError:
                     self.driver=None
                 #self.mutex.release()
            return self.driver
        except WebDriverException:
            raise
