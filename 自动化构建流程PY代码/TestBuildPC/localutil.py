#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import os
import sys
import subprocess
import email_notify


def executeSpecialCmdBeforePack():
    pass


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
    time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    return time_str


# 获得当前除disable外的参数
def get_current_argv_without_disable():
    append_args = ""
    if len(sys.argv) > 1:
        for item in sys.argv:
            if item != "Disable" and item != "disable":
                append_args += " " + item
    return append_args


# 检测该脚本是否被禁用
def check_disable():
    isDisable = False
    if len(sys.argv) > 1:
        for item in sys.argv:
            if item == "Disable" or item == "disable":
                isDisable = True
    log("是否开启此PY is_disable : %s" % isDisable)
    return isDisable


def exit_fail():
    log("exit fail")
    email_notify.send_mail(False)
    sys.exit(-1)


def exit_success():
    log("exit success")
    email_notify.send_mail(True)

# <editor-fold desc = "git 相关">
# 配置git 上传的用户名、永久显式保存用户名密码、大小写敏感
def git_config():
    execute('git config --global user.name "packPC"')
    execute('git config --global user.password "packPC"')
    execute('git config credential.helper store')  # 此命令将证书无限期地存储在磁盘上，以供将来的Git程序使用。
    execute('git config --global core.ignorecase false')   # 全局设置 大小写敏感 防止拿到错误文件


# 针对一周前的每一条git log信息，每一个提交匯聚成列表，以 哈希、详细信息 的形式存在縂表里
def git_log():
    git_cmd_log = 'git log --since="1 weeks ago" --pretty=format:"%H %s %cn" --no-merges'
    subprocess1 = subprocess.Popen(git_cmd_log, stdout=subprocess.PIPE)
    git_infos_str = subprocess1.stdout.read().decode()
    git_infos_list = git_infos_str.split('\n')
    git_log_list_desc_list = []
    for git_infos_item in git_infos_list:
        git_infos_item_list = git_infos_item.split(' ')
        git_hash = git_infos_item_list[0]
        git_desc = git_infos_item_list[1:len(git_infos_item_list)]
        git_infos_desc_list = [git_hash, git_desc]
        git_log_list_desc_list.append(git_infos_desc_list)
    return git_log_list_desc_list


# 两个log集合进行差异输出
def git_diff_log(git_info_before, git_info_after, git_log_path):
    diff_log_hash = set()
    for git_info in git_info_before:
        diff_log_hash.add(git_info[0])
    print("==========================================================================================")
    index = 1
    git_logs = ' '
    for git_info in git_info_after:
        if git_info[0] not in diff_log_hash:
            desc_info = ' '
            for item in git_info[1]:
                desc_info = desc_info + " " + item
            print("[" + str(index) + "]" + desc_info)
            git_logs = git_logs + desc_info + '\n'
            index = index + 1
    print("==========================================================================================")
    git_log_text(git_logs, git_log_path)


def git_log_text(git_infos, git_log_path):
    log_file = open(git_log_path, 'w', encoding='utf8')
    log_file.write(git_infos)
    log_file.close()


# 切换到指定git 指定分支
def git_update(git_url, git_branch):
    execute('git checkout .')
    execute('git clean -df')
    execute('git reset --hard HEAD^')
    execute('git remote set-url origin ' + git_url)
    execute('git checkout -b ' + git_branch + ' origin/' + git_branch)
    execute('git checkout ' + git_branch)
    execute('git pull')
# </editor-fold>
