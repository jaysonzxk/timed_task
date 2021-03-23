import os
import pandas as pd


def get_test_data(file_path, sheet_name, n):
    """
    pandas读取表格数据
    :param file_path:
    :param sheet_name:
    :param n: 表格行数（1表示第一行）
    :return:
    """
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    s = pd.ExcelFile(file_path)
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    df = s.parse()
    k_list = list(df.keys())
    v_list = data.values.tolist()
    data_dict = dict(zip(k_list, v_list[n]))
    return data_dict