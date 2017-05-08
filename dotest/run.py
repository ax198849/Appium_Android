#coding=utf-8
import os
from common import readConfig as readConfig
from common.driver import MyDriver
from common.AppiumServer import AppiumServer
import common.Log as Log
from time import sleep
import unittest
from common import HTMLTestRunner
from urllib2 import URLError
import os
import threading
import ctypes
import inspect

readConfigLocal=readConfig.ReadConfig()

baseurl=readConfigLocal.getConfigValue('baseUrl')

dir = os.path.split(os.path.realpath(__file__))[0]

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

mylock=threading.RLock()

class myServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.myserver = AppiumServer()

    def run(self):
        self.myserver.run_server()


class Alltest(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        global log,logger,resultPath
        self.caselistPath=os.path.join(readConfig.prjDir,'caseList.txt')
        self.casePath=os.path.split(os.path.realpath(__file__))[0]
        self.caseList=[]
        #self.myserver=AppiumServer()
        log=Log.Log()
        logger=log.get_my_logger()
        resultPath=log.get_result_path()

    def driver_on(self):
        MyDriver().get_driver()

    def driver_off(self):
        pass

    def set_case_list(self):
        fp=open(self.caselistPath)

        for data in fp.readlines():
            s_data=str(data)
            if s_data != '' and not s_data.startswith('#'):
                self.caseList.append(s_data.replace('\n',''))
            fp.close()

    def create_suite(self):
        self.set_case_list()
        test_suite=unittest.TestSuite()
        suite_model_list=[]

        if len(self.caseList)>0:

            for case_name in self.caseList:

                discover=unittest.defaultTestLoader.discover(self.casePath,pattern=case_name+'.py',top_level_dir=None)
                suite_model_list.append(discover)

        if len(suite_model_list)>0:

            for suite in suite_model_list:
                 for test_name in suite:
                     test_suite.addTest(test_name)
        else:
            return None

        return test_suite


    def run(self):

        try:
            suit=self.create_suite()
            if suit is not None:
                #logger.info("Begin to start Appium Server")
                #self.myserver.run_server()

                #logger.info("End to start Appium Server")
                #logger.info("open Driver")
                self.driver_on()
                logger.info('Start to test')
                fp=open(resultPath,'wb')
                runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='testReport',description='Report_description')
                runner.run(suit)
                logger.info('End to test')
            else:
                logger.info('Have no test to run')

        except Exception as e:
            logger.error(str(e))
            raise

        finally:
            try:
                #logger.info('Close to Driver')
                self.driver_off()
                #logger.info('Begin stop Appium Server')

                print 'ok'
                #logger.info('End stop Appium Server')

            except URLError as e:
                logger.info(str(e))

            except KeyError as e:
                logger.info(str(e))

def _async_raise(tid,exctype):
    tid=ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype=type(exctype)
    res=ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,ctypes.py_object(exctype))
    if res == 0:
        raise ValueError('invalid thread id')
    elif res !=1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,None)
        raise SystemError('PyThreadState_SetAsyncExc Failed')

def stop_thread(thread):
    _async_raise(thread.ident,SystemExit)


if __name__=='__main__':
    thread1=myServer()
    thread2=Alltest()
    thread1.start()
    sleep(5)
    thread2.start()
    while thread2.is_alive():
        sleep(2)
    else:
        stop_thread(thread1)
        #stop_thread(thread1)

    print 'aixuxuxuxuuxuxuxuxuxuxuux'





