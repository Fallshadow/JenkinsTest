#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 作者: lhs
# 时间: 2021.02.22
# 用途: 拷贝刚生成的apk到指定Jenkins目录
#######################################################

import os
import shutil
import time
import subprocess
import localutil

SRC_APK_PATH = 'G:/jenkinsworkspace/rex_client_android/apk/'
DEST_APK_PATH = 'E:/Jenkins/workspace/rex_client_android/apk/'

BUILD_TIMESTAMP = os.getenv("BUILD_TIMESTAMP")

def copy_files():
    localutil.log("开始拷贝apk")
    src_file = SRC_APK_PATH  + "rex_" + BUILD_TIMESTAMP + ".apk"
    dest_file = DEST_APK_PATH + "rex_" + BUILD_TIMESTAMP + ".apk"
    shutil.copyfile(src_file,dest_file)
    localutil.log(("结束拷贝apk")

def main():
    copy_files()

if __name__ == "__main__":
    if localutil.check_disable():
        localutil.log("disable")
    else:
        main()