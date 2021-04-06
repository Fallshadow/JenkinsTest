#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os.path
import localutil
import compilerlog

# 基础配置
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1803442018@qq.com"  # 用户名
mail_pass = "symwuxaaoilvbigf"  # 口令
mail_port = 465
sender = '1803442018@qq.com'
# 接收邮件列表
receivers = ['1803442018@qq.com']

# 获取Jenkins变量
BUILD_ID = os.getenv("BUILD_ID")
JOB_NAME = os.getenv("JOB_NAME")
BUILD_NUMBER = os.getenv("BUILD_NUMBER")
BUILD_URL = os.getenv("BUILD_URL")
BUILD_TIMESTAMP = os.getenv("BUILD_TIMESTAMP")
JOB_URL = os.getenv("JOB_URL")

BUILD_STATUS = "Success"


def construct_fail_html():
    html_msg = '''
    <!DOCTYPE html>    
    <html>    
    <head>    
    <meta charset="UTF-8">    
    <title>IOS打包机第''' + BUILD_NUMBER + '''次构建日志</title>    
    </head>    

    <body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4"    
        offset="0">    
        <table width="95%" cellpadding="0" cellspacing="0"  style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">    
            <tr>    
                本邮件由系统自动发出，无需回复！<br/>            
                各位同事，大家好，以下为''' + JOB_NAME + '''项目构建信息</br> 
                <td><font color="#CC0000">构建结果 - ''' + BUILD_STATUS + '''</font></td>   
            </tr>    
            <tr>    
                <td><br />    
                <b><font color="#0B610B">构建信息</font></b>    
                <hr size="2" width="100%" align="center" /></td>    
            </tr>    
            <tr>    
                <td>    
                    <ul>    
                        <li>项目名称 ： ''' + JOB_NAME + '''</li>    
                        <li>构建编号 ： 第''' + BUILD_NUMBER + '''次构建</li>    
                        <li>构建状态： ''' + BUILD_STATUS + '''</li>    
                        <li>构建日志： <a href="''' + BUILD_URL + '''console">''' + BUILD_URL + '''console</a></li>      
                        <li>工作目录 ： <a href="''' + JOB_URL + '''ws">''' + JOB_URL + '''ws</a></li>     
                    </ul>    
                </td>
            </tr>
            <tr>    
                <td><br />    
                <b><font color="#2B683B">失败原因</font></b>    
                <hr size="2" width="100%" align="center" /></td>    
            </tr>    
            <tr>
                <td>
                    <ul>
                        <li>''' + compilerlog.get_fail_log() + ''' </li>
                    </ul>
                </td>
            </tr>
        </table>    
    </body>    
    </html>    
    '''
    return html_msg


def construct_success_html():
    html_msg = '''
    <!DOCTYPE html>    
    <html>    
    <head>    
    <meta charset="UTF-8">    
    <title>IOS打包机第''' + BUILD_NUMBER + '''次构建日志</title>    
    </head>    

    <body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4"    
        offset="0">    
        <table width="95%" cellpadding="0" cellspacing="0"  style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">    
            <tr>    
                本邮件由系统自动发出，无需回复！<br/>            
                各位同事，大家好，以下为''' + JOB_NAME + '''项目构建信息</br> 
                <td><font color="#CC0000">构建结果 - ''' + BUILD_STATUS + '''</font></td>   
            </tr>    
            <tr>    
                <td><br />    
                <b><font color="#0B610B">构建信息</font></b>    
                <hr size="2" width="100%" align="center" /></td>    
            </tr>    
            <tr>    
                <td>    
                    <ul>    
                        <li>项目名称 ： ''' + JOB_NAME + '''</li>    
                        <li>构建编号 ： 第''' + BUILD_NUMBER + '''次构建</li>    
                        <li>构建状态： ''' + BUILD_STATUS + '''</li>    
                        <li>构建日志： <a href="''' + BUILD_URL + '''console">''' + BUILD_URL + '''console</a></li>      
                        <li>工作目录 ： <a href="''' + JOB_URL + '''ws">''' + JOB_URL + '''ws</a></li>     
                    </ul>    
                </td>
            </tr>
        </table>    
    </body>    
    </html>    
    '''
    return html_msg


def send_mail(succ=True):
    global BUILD_STATUS
    mail_content = ""
    if succ:
        BUILD_STATUS = "成功"
        mail_content = construct_success_html()
    else:
        BUILD_STATUS = "失败"
        mail_content = construct_fail_html()

    # 第三方 SMTP 服务
    message = MIMEText(mail_content, 'html', 'utf-8')
    message['From'] = Header("PC打包机", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = '【构建通知】 PC版本 Build #' + BUILD_ID + ' ' + BUILD_STATUS
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        localutil.log("邮件发送成功")
    except smtplib.SMTPException:
        localutil.log("Error: 无法发送邮件")

