"""
author： mask
filename: review_task.py
datetime： 2021/3/23 19:11 
ide： PyCharm
"""
import json
import time
import requests
from common.logger import Log as log
from common.bms_login import getBmsToken
from common.get_page_data import getData


class Review:
    """
    审核
    """
    def __init__(self):
        self.id_list = getData().get_data()

    def review_money(self):
        url = 'http://192.168.0.201:8041/admin/income/check'
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': getBmsToken().get_token()
        }
        for item in self.id_list:
            data = {"id": item, "auditState": "RECHARGE_SUCCESS"}
            res = requests.post(url, data=json.dumps(data), headers=headers)
            log().info('接口返回{}'.format(res.json()))
            time.sleep(0.5)