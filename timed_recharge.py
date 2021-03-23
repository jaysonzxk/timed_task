"""
author： mask
filename: timed_recharge.py
datetime： 2021/3/23 16:31 
ide： PyCharm
"""
from jsonpath import jsonpath
import requests
import json
from common.app_login import getAppToken
from common import bms_login
from common.tojsonstr import getJsonStr
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from common.logger import Log as log


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
            log().info(message='充值次数{}，接口返回{}'.format(i, res))
            time.sleep(0.5)


class GetData:
    def __init__(self):
        self.data = {
            "pageParam": {
                "current": 1,
                "size": 100,
                "orderBy": "update_time",
                "orderType": "desc"
            },
            "searchParam": {
                "i_auditState": "",
                "i_changeMoney": [

                ],
                "i_id": "",
                "maxAmout": "",
                "minAmout": "",
                "i_incomeMoneyByType": "",
                "i_type": "",
                "suu_levelId": "",
                "i_userId": "",
                "suupdate_username": "",
                "suu_username": "python110",
                "suu_isOperate": False,
                "createTime": [
                    "2021-03-22 00:00:00",
                    "2021-03-23 23:59:59"
                ],
                "startTime": "2021-03-22 00:00:00",
                "endTime": "2021-03-23 23:59:59"
            }
        }
        self.url = 'http://192.168.0.201:8041/admin/income/getPage'
        self.headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': bms_login.get_token()
        }

    def get_data(self):
        resp = requests.post(self.url, data=json.dumps(self.data), headers=self.headers)
        try:
            res = getJsonStr(resp.json()['data']).get_json_str()
            res_list = jsonpath(res, "$..data.records[*].id")
            return res_list
        except:
            pass


class Review:
    def __init__(self):
        self.id_list = GetData().get_data()

    def review_money(self):
        url = 'http://192.168.0.201:8041/admin/income/check'
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': bms_login.get_token()
        }
        # print(self.id_list)
        # exit()
        n = 0
        for item in self.id_list:
            data = {"id": item, "auditState": "RECHARGE_SUCCESS"}
            res = requests.post(url, data=json.dumps(data), headers=headers)
            log().info('接口返回{}'.format(res.json()))
            time.sleep(0.5)


def job_Recharge():
    Recharge().recharge_money()


def job_review():
    Review().review_money()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job_Recharge, 'date', run_date='2021-03-23 23:55:00')
    scheduler.add_job(job_review, 'date', run_date='2021-03-24 00:05:00')
    scheduler.start()
