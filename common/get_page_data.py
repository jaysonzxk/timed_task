"""
author： mask
filename: get_page_data.py
datetime： 2021/3/23 19:12 
ide： PyCharm
"""
import json
import requests
from jsonpath import jsonpath
from common.bms_login import getBmsToken
from common.tojsonstr import getJsonStr


class getData:
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
            'Authorization': getBmsToken().get_token()
        }

    def get_data(self):
        resp = requests.post(self.url, data=json.dumps(self.data), headers=self.headers)
        try:
            res = getJsonStr(resp.json()['data']).get_json_str()
            res_list = jsonpath(res, "$..data.records[*].id")
            return res_list
        except:
            pass
