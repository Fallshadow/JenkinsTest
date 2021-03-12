#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 作者: lhs
# 时间: 2021.02.20
# 用途: 通用函数
#######################################################

import os
import sys
import datetime
import email_notify

#执行系统命令
def execute(cmd):
    log("execute cmd >> " + cmd)
    os.system(cmd)

#获得当前时间
def get_current_time():
	now_time = datetime.datetime.now()
	time_str = datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
	return time_str

#输出带时间的log
def log(*args):
	logMsg = "[Log][" + get_current_time() + "] "
	for item in args:
	 	logMsg = logMsg + str(item)
	print(logMsg)

#检测该脚本是否被禁用
def check_disable():
    isDisable = False
    if(len(sys.argv) > 1):
        for item in sys.argv:
            if item == "Disable" or item == "disable":
                isDisable = True
    return isDisable

def exit_fail(xcodeFail = False):
    log("exit fail")
    email_notify.send_mail(False,xcodeFail)
    sys.exit(-1)