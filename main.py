#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import datetime

PATTEN = [  # 图形矩阵，行建议最多不超过7行
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
]


def calculate_date(start, end):
    # 计算日期相差天数
    start_sec = time.mktime(time.strptime(start, '%Y-%m-%d'))
    end_sec = time.mktime(time.strptime(end, '%Y-%m-%d'))

    days = int((end_sec - start_sec) / (24 * 60 * 60))

    return days


def commit(flag):
    if flag:
        for n in range(39):  # 设置commit次数
            with open('./electrocardiogram.txt', 'a') as record:
                record.write('.')
                record.close()
                os.system('git commit -a -m \"HeartBeat\"')

    else:  # 每天推一条
        with open('./electrocardiogram.txt', 'a') as record:
            record.write('.~^~')
            record.close()
            os.system('git commit -a -m \"HeartBeat\"')

    os.system('git pull && git push origin master')


PERIOD = len(PATTEN[0])  # 周期(图案列数)

START_DATE = '2017-7-16'  # 开始日期
now = datetime.datetime.now().strftime('%Y-%m-%d')

row = calculate_date(START_DATE, now) % 7
col = int(calculate_date(START_DATE, now) / 7) % PERIOD

commit(PATTEN[row][col])

# 00 12 * * * cd /home/git_heart && git pull && /usr/bin/python main.py
