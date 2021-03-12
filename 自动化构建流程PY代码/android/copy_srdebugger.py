#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 作者: lhs
# 时间: 2021.02.22
# 用途: 拷贝SR Debugger工具到工程中
#######################################################

import _thread
import time
import os
import datetime
import shutil
import distutils
import distutils.dir_util
import sys
import localutil

SRC_PATH = "G:/jenkinsworkspace/rex_client_android/SRDebug/StompyRobot"
DEST_PATH = "G:/jenkinsworkspace/rex_client_android/rex_client/Assets/StompyRobot"

def copy_files():
    distutils.dir_util.copy_tree(SRC_PATH,DEST_PATH)

if __name__ == "__main__":
    if localutil.check_disable():
        localutil.log("disable")
    else:
        localutil.log("enable")
        copy_files()