"""
author： mask
filename: base.py
datetime： 2021/3/19 0:26 
ide： PyCharm
"""
from common.requestmethod import myRequestMethod


def get_response(url, method, **kwargs):
    if method == "get":
        resp = myRequestMethod().get(url, **kwargs)
    if method == "post":
        resp = myRequestMethod().post(url, **kwargs)
    if method == "delete":
        pass
    if method == "put":
        pass
    return resp
