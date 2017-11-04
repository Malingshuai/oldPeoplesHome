# -*- coding: utf8 -*-

import csv

def get_csv_data(csv_path):
    """read test data from csv and return as list
    从CSV读取测试数据并返回列表
    @type csv_path: string
    @param csv_path: some csv path string
    @return list
    """
    rows = []
    try:
        csv_data = open(str(csv_path), "rb")
    except:
        print u'文件 %s 打开失败！' % csv_data

    content = csv.reader(csv_data)

    # skip header line 跳过标题行
    next(content, None)

    # add rows to list
    for row in content:
        rows.append(row)

    return rows