#coding=utf-8

#定义读取配置文件的方法

import ConfigParser
import os

prjDir = os.path.split(os.path.realpath(__file__))[0]
configfile_path = os.path.join(prjDir, "config.ini")

class ReadConfig:
    def __init__(self):
        self.cf=ConfigParser.ConfigParser()
        self.cf.read(configfile_path)

    def getConfigValue(self,name):
        value=self.cf.get('config',name)
        return value

    def getCmdValue(self,name):
        value=self.cf.get('cmd',name)
        return value