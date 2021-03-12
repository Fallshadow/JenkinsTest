#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 作者: lhs
# 时间: 2021.02.22
# 用途: 将apk上传至ftp服务器
#######################################################


import os
import shutil
import time
import subprocess
import sys
import localutil

from ftplib import FTP


FTP_IP = "10.15.120.92"
FTP_PORT = 21
FTP_USERNAME = "clientpkg"
FTP_PASSWORD = "clientpkg123"

SRC_APK_PATH = "G:/jenkinsworkspace/rex_client_android/apk/"
DEST_APK_PATH = "/client_pkg/rex/apk/"

BUILD_TIMESTAMP = os.getenv("BUILD_TIMESTAMP")
# BUILD_TIMESTAMP = "2020-11-26_09-56-11"

def upload_to_ftp():
    ftp = FTP()
    localutil.log(("开始尝试连接ftp服务器")
    ftp.connect(FTP_IP,FTP_PORT)
    localutil.log(("开始尝试登录ftp服务器")
    ftp.login(FTP_USERNAME,FTP_PASSWORD)
    src_file = SRC_APK_PATH  + "rex_" + BUILD_TIMESTAMP + ".apk"
    dest_file = DEST_APK_PATH + "rex_" + BUILD_TIMESTAMP + ".apk"
    if not os.path.isfile(src_file):
        localutil.log(("文件" + src_file + "不存在，取消上传")
        return
    fp = open(src_file,'rb')
    localutil.log(("开始上传文件到ftp服务器")
    ftp.storbinary("STOR %s" % dest_file,fp)
    localutil.log(("上传结束，关闭句柄")
    fp.close()
    ftp.close()

def main():
    upload_to_ftp()

if __name__ == "__main__":
    if(not localutil.check_disable()):
        main()
