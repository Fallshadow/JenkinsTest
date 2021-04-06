#!/usr/bin/python
# -*- coding: UTF-8 -*-

import localconfig
import _thread
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os.path
import localutil
import subprocess
import shutil
import datetime


from ftplib import FTP


def upload_to_ftp():
    ftp = FTP()
    localutil.log("开始尝试连接ftp服务器")
    ftp.connect(localconfig.FTP_IP, localconfig.FTP_PORT)
    localutil.log("开始尝试登录ftp服务器")
    ftp.login(localconfig.FTP_USERNAME, localconfig.FTP_PASSWORD)
    src_file = localconfig.SRC_EXE_PATH + "Test.txt"
    ftp_file = localconfig.FTP_EXE_PATH + "Test.txt"
    if not os.path.isfile(src_file):
        localutil.log("文件" + src_file + "不存在，取消上传")
        return
    fp = open(src_file, 'rb')
    localutil.log("开始上传文件到ftp服务器")
    ftp.storbinary("STOR %s" % ftp_file, fp)
    localutil.log("上传结束，关闭句柄")
    fp.close()
    ftp.close()


# 基础配置
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1803442018@qq.com"  # 用户名
mail_pass = "symwuxaaoilvbigf"  # 口令
mail_port = 465
sender = '1803442018@qq.com'
# 接收邮件列表
receivers = ['1803442018@qq.com']


def email_test():
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print
        "邮件发送成功"
    except smtplib.SMTPException:
        print
        "Error: 无法发送邮件"


# 获取Jenkins变量
BUILD_ID = os.getenv("BUILD_ID")
JOB_NAME = os.getenv("JOB_NAME")
BUILD_NUMBER = os.getenv("BUILD_NUMBER")
BUILD_URL = os.getenv("BUILD_URL")
BUILD_TIMESTAMP = os.getenv("BUILD_TIMESTAMP")
JOB_URL = os.getenv("JOB_URL")


def jenkins_args_test():
    print("BUILD_ID" + BUILD_ID)
    print("JOB_NAME" + JOB_NAME)
    print("BUILD_NUMBER" + BUILD_NUMBER)
    print("BUILD_URL" + BUILD_URL)
    print("BUILD_TIMESTAMP" + BUILD_TIMESTAMP)
    print("JOB_URL" + JOB_URL)


def compress_test():
    localutil.execute("C:/Windows/Rar.exe a -r- -ag" + localconfig.BUILD_TIMESTAMP + " -ep1 -df D:/Test/ACT_PC_ D:/Test/p*/")
    # nowTime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')
    # localutil.log(nowTime)
    # shutil_test(nowTime)


def shutil_test(nowTime):
    shutil.copyfile("D:/Test/ACT_PC_" + nowTime + ".rar", "D:/Test/mytest/ACT_PC_" + nowTime + ".rar")


def param_test():
    nowTime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')
    localconfig.LOCAL_BUILD_TIMESTAMP_STR = nowTime
    localutil.log(localconfig.LOCAL_BUILD_TIMESTAMP_STR)


if __name__ == '__main__':
    if localutil.check_disable():
        localutil.log("disable")
    else:
        compress_test()
        # shutil.copyfile("D:/Test/act_pc_2021-04-06-09-52-19.rar", "D:/Test/mytest/mytest.rar")
