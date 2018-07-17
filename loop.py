#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import datetime


def calculate_date(start, end):
    # 计算日期相差天数
    start_sec = time.mktime(time.strptime(start, '%Y-%m-%d'))
    end_sec = time.mktime(time.strptime(end, '%Y-%m-%d'))

    days = int((end_sec - start_sec) / (24 * 60 * 60))

    return days


def add_days(d, num):
    # 日期递增
    sec = num * 24 * 60 * 60
    now_sec = time.mktime(time.strptime(d, '%Y-%m-%d')) + sec
    return time.strftime("%Y-%m-%d", time.localtime(now_sec))


def commit(flag):
    if flag:
        for n in range(39):
            with open('./record.txt', 'a') as record:
                record.write('.~^~')
                record.close()
                os.system('git commit -a -m \"HeartBeat\"')

        with open('./record.txt', 'a') as record:
            record.write('\n')
            record.close()
            os.system('git commit -a -m \"HeartBeat\"')

    else:
        with open('./record.txt', 'a') as record:
            record.write(now + '\n')
            record.close()
            os.system('git commit -a -m \"HeartBeat\"')


with open('./model.json') as f:  # 加载模型
    PATTEN = f.read()
    f.close()

PERIOD = len(PATTEN[0])  # 周期(图案列数)

START_DATE = '2017-7-16'  # 开始日期, 码云和git显示不一样, 建议从最左上角开始
now = datetime.datetime.now().strftime('%Y-%m-%d')

while calculate_date(START_DATE, now) >= 0:
    row = calculate_date(START_DATE, now) % 7
    col = int(calculate_date(START_DATE, now) / 7) % PERIOD
    commit(PATTEN[row][col])

    now = add_days(now, -1)
    os.system('timedatectl set-time ' + now)

#  复原时间
os.system('timedatectl set-ntp 1 && timedatectl set-local-rtc 1')


