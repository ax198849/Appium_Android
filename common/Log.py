import logging
import readConfig as readConfig
import time
from time import sleep
import os

class Log:

    def __init__(self):
        global logger,resultPath,logPath
        resultPath=os.path.join(readConfig.prjDir,'result')
        logPath=os.path.join(resultPath,(time.strftime('%Y%m%d%H%M%S',time.localtime())))
        if os.path.exists(logPath) is False:
            os.makedirs(logPath)
        self.checkNo=0
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.INFO)


        fh=logging.FileHandler(os.path.join(logPath,'outPut.log'))


        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    def get_result_path(self):

        report_path=os.path.join(logPath,'report.html')
        return  report_path

    def get_my_logger(self):

        return self.logger

    def build_start_line(self, case_no):


        start_line = "----  " + case_no + "   START     ----"
        self.logger.info(start_line)

    def build_end_line(self, case_no):

        end_line = "----  " + case_no + "   END     ----"
        self.logger.info(end_line)
        self.checkNo = 0

    def write_result(self, result):

        report_path = os.path.join(logPath, "report.txt")
        flogging = open(report_path, "a")
        try:
            flogging.write(result + "\n")
        finally:
            flogging.close()
        pass

    def take_shot(self, driver, case_name):

        screenshot_name = str(self.checkNo) + ".png"
        screenshot_path = os.path.join(logPath, case_name)

        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        screenshot = os.path.join(screenshot_path, screenshot_name)


        sleep(1)
        driver.get_screenshot_as_file(screenshot)
        self.checkNo += 1

        return os.path.join(screenshot.replace(resultPath, "../../result"))


