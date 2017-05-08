#coding=utf-8
import os
import threading
import readConfig as readConfig
from urllib2 import urlopen
from urllib2 import URLError
from multiprocessing import Process
from init_phone import Getphoneinfo

readConfigLocal=readConfig.ReadConfig()

class AppiumServer:

    def __init__(self):
        self.openAppium=readConfigLocal.getCmdValue('openAppium')
        self.baseUrl=readConfigLocal.getConfigValue('baseUrl')
        self.stopAppium=readConfigLocal.getCmdValue('stopAppium')

    def run_server(self):
        phone_state=Getphoneinfo().connect_phone()
        if cmp(phone_state,'unknown')== 1:
            raise ValueError('手机状态不正确,请保证手机正常连接电脑')
        else:
            self.stop_server()
            Getphoneinfo().restart_daemon()
            phone_id=str(Getphoneinfo().get_phone_id())
            os.system(self.openAppium+''+phone_id)
            #t1=RunServer(self.openAppium+''+phone_id)
            #p=Process(target=t1.start())
            #p.start()

    def stop_server(self):
        os.system(self.stopAppium)

    def is_running(self):
        response=None
        url=self.baseUrl+"/status"
        try:
            response=urlopen(url,timeout=5)
            if str(response.getcode()).startswith('2'):
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()

class RunServer(threading.Thread):
    def __init__(self,cmd):
        threading.Thread.__init__(self)
        self.cmd=cmd

    def run(self):
        os.system(self.cmd)

