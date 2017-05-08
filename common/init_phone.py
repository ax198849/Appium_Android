import readConfig
import os

readConfigLocal=readConfig.ReadConfig()

class Getphoneinfo:
    def __init__(self):
        self.checkPhone=readConfigLocal.getCmdValue('checkPhone')
        self.viewAndroid=readConfigLocal.getCmdValue('viewAndroid')
        self.viewPhone=readConfigLocal.getCmdValue('viewPhone')
        self.phoneName=readConfigLocal.getConfigValue('phoneName')
        self.start_daemon=readConfigLocal.getCmdValue('startServer')
        self.close_daemon=readConfigLocal.getCmdValue('closeServer')

    def connect_phone(self):
        value=os.popen(self.checkPhone).read()
        return value

    def get_android_version(self):
        version=str(os.popen(self.viewAndroid).read())
        if version!='':
            pop = version.rfind(str('='))
            return version[pop+1:]
        else:
            return None

    def get_phone_id(self):
        phone_id=str(os.popen(self.viewPhone).read())
        if phone_id!='':
            id=phone_id.split()
            return id[4]
        else:
            return None

    def get_phone_name(self):
        name=self.phoneName
        return name

    def start_phone_server(self):
        os.system(self.start_daemon)

    def close_phone_server(self):
        os.system(self.close_daemon)

    def restart_daemon(self):
        self.close_phone_server()
        self.start_phone_server()




