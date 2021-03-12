#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 作者: lhs
# 时间: 2021.02.22
# 用途: Git更新主工程
#######################################################


import os
import sys
import subprocess
import shutil, errno
import glob
import fnmatch
import datetime
import localutil


GIT_URL = "http://10.15.120.11/root/rex_client.git"
GIT_BRANCH = "master"
CD_ROOT = "G:/jenkinsworkspace/rex_client_android/rex_client"
GIT_LOG_FILE_PATH = "G:/jenkinsworkspace/rex_client_android/gitlog.txt"


def git_oper():
    localutil.execute('git config --global user.password "CP12cp34"')
    localutil.execute('git config --global user.name "clientpublish"')
    localutil.execute('git config credential.helper store')
    localutil.execute('git config --global core.ignorecase false')
    if os.path.exists(".git"):
        all_infos = collect_all()
        git_infos = collect_git(all_infos)
        # localutil.execute("git fetch -a")
        localutil.execute("git checkout .")
        localutil.execute("git clean -fd")
        localutil.execute("git reset --hard HEAD^")
        localutil.execute("git remote set-url origin " + GIT_URL)
        localutil.execute("git  checkout -b " + GIT_BRANCH + " origin/" + GIT_BRANCH)
        localutil.execute("git checkout " + GIT_BRANCH)
        localutil.execute("git pull")

        all_infos2 = collect_all()
        git_infos2 = collect_git(all_infos2)
        check_diff(git_infos,git_infos2)
    else:
        localutil.execute("git init")
        localutil.execute("git remote add -f origin " + GIT_URL)
        localutil.execute("git config core.sparsecheckout true")
        localutil.execute("git pull origin " + GIT_BRANCH)
    # localutil.execute("git fetch --all")
    # localutil.execute("git reset --hard origin/" + GIT_BRANCH)
    # localutil.execute("git checkout " + GIT_BRANCH)

def check_diff(git_infos,git_infos2):
    temp_hash = set()
    for item in git_infos:
        temp_hash.add(item[0])
    print("==========================================================================================")
    index = 1
    git_logs = ''
    for item in git_infos2:
        if item[0] not in temp_hash:
            print("[" + str(index) + "]" + item[1])
            git_logs = git_logs + item[1] + '\n'
            index = index + 1
    print("==========================================================================================")
    save_log_file(git_logs)

def main():
    localutil.log("Start git update")
    os.chdir(CD_ROOT)
    git_oper()
    localutil.log("End git update")

def processArgu():
    global GIT_BRANCH
    if(len(sys.argv) > 1):
        localutil.log("switch branch to : " + sys.argv[1])
        GIT_BRANCH = sys.argv[1]

def collect_git(all_info):
    split_datas = all_info.split('\n')
    list_all_info = []
    current_index = -1
    for split_data in split_datas:
        items = split_data.split(' ')
        origin_str_len = len(split_data)
        githash = items[0]
        githash_len = len(githash)
        gitdesc = split_data[githash_len:origin_str_len]
        gititem = [githash,gitdesc]
        list_all_info.append(gititem)
    return list_all_info

def collect_all():
    # archiveCmd = 'git log -n 30 --pretty=format:"%H %s" --no-merges'
    archiveCmd = 'git log --since="1 weeks ago" --pretty=format:"%H %s" --no-merges'
    child1 = subprocess.Popen(archiveCmd, stdout=subprocess.PIPE)
    allinfo = child1.stdout.read().decode()
    # print(allinfo)
    return allinfo

def save_log_file(git_logs):
    log_file = open(GIT_LOG_FILE_PATH,'w',encoding='utf8')
    log_file.write(git_logs)
    log_file.close()

if __name__ == "__main__":
    if(not localutil.check_disable()):
        processArgu()
        main()


