#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import time
import subprocess
import sys
import localutil
import localconfig

from ftplib import FTP


def upload_to_ftp():
    ftp = FTP()
    localutil.log("开始尝试连接ftp服务器")
    ftp.connect(localconfig.FTP_IP, localconfig.FTP_PORT)
    localutil.log("开始尝试登录ftp服务器")
    ftp.login(localconfig.FTP_USERNAME, localconfig.FTP_PASSWORD)
    src_file = localconfig.SRC_EXE_PATH + localconfig.GIT_PROJECT_COMPRESS_NAME + localconfig.BUILD_TIMESTAMP + ".rar"
    ftp_file = localconfig.FTP_EXE_PATH + localconfig.GIT_PROJECT_COMPRESS_NAME + localconfig.BUILD_TIMESTAMP + ".rar"
    if not os.path.isfile(src_file):
        localutil.log("文件" + src_file + "不存在，取消上传")
        return
    fp = open(src_file, 'rb')
    localutil.log("开始上传文件到ftp服务器")
    ftp.storbinary("STOR %s" % ftp_file, fp)
    localutil.log("上传结束，关闭句柄")
    fp.close()
    ftp.close()


def main():
    upload_to_ftp()


if __name__ == "__main__":
    if not localutil.check_disable():
        main()
