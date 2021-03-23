#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import os
import sys


# 执行系统命令
def execute(cmd):
    log("execute cmd >> " + cmd)
    os.system(cmd)


# 输出带时间的log
def log(*args):
    logMsg = "[log][" + get_current_time() + "]"
    for item in args:
        logMsg = logMsg + str(item)
    print(logMsg)


# 获得当前时间
def get_current_time():
    now_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
    return time_str


# 获得当前除disable外的参数
def get_current_argv_without_disable():
    append_args = ""
    if(len(sys.argv) > 1):
        for item in sys.argv:
            if item != "Disable" and item != "disable":
                append_args += " " + item
    return time_str


# 检测该脚本是否被禁用
def check_disable():
    isDisable = False
    if len(sys.argv) > 1:
        for item in sys.argv:
            if item == "Disable" or item == "disable":
                isDisable = True
    return isDisable
