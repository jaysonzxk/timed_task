"""
author： mask
filename: tojsonstr.py
datetime： 2021/3/19 12:06 
ide： PyCharm
"""
from common.base import get_response
from test_data.read_data import get_test_data
from common.logger import Log
import json


class getJsonStr:
    """
    解析接口返回加密数据
    """
    def __init__(self, value):
        self.value = value  # 要解析的数据
        self.log = Log()  # 日志
        self.test_data = get_test_data('test_data.xlsx', 'common', 0)
        self.url = self.test_data['url']
        self.headers = self.test_data['header']
        self.method = self.test_data['method']
        self.payload = {
            'value': self.value
        }

    def get_json_str(self):
        try:
            res = get_response(self.url, method=self.method, headers=json.loads(self.headers), data=json.dumps(self.payload)).json()
            self.log.info('正在解析加密数据==========')
            # self.log.info('解析结果为: {}'.format(res))
            return res
        except Exception as e:
            print('请求错误{}'.format(e))
