"""
author： mask
filename: recharge_task.py
datetime： 2021/3/23 19:15 
ide： PyCharm
"""
import json
import time
import requests
from common.logger import Log as log
from common.app_login import getAppToken


class Recharge:
    """
    充值
    """
    def __init__(self):
        # self.log = Log()
        self.url = 'http://192.168.0.201:8071/admin/appFinance/saveByOffice'
        self.data = json.dumps(
            {
                "officeAccountId": 3,
                "payMoney": 2000000,
                "payName": "",
                "transferVoucherUrl": "https://zxbuk.oss-cn-hongkong.aliyuncs.com/certificate/16fcab357d3c4675810d2d6acf4fd2b5.jpg"
            }
        )
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': getAppToken().get_token()
        }

    def recharge_money(self):
        for i in range(100):
            res = requests.post(self.url, data=self.data, headers=self.headers).json()
            log().info(message='充值次数{}，接口返回{}'.format(i+1, res))
            time.sleep(0.5)