#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 作者: lhs
# 时间: 2021.02.22
# 用途: 上传文件到git
#######################################################

import os
import shutil
import time
import subprocess
import localutil

CD_ROOT = 'G:/jenkinsworkspace/rex_client_android/rex_client/'
COPY_SRC_PATH = 'G:/jenkinsworkspace/rex_client_android/tempdata/'
COPY_DEST_PATH = 'G:/jenkinsworkspace/rex_client_android/rex_client/'
COPY_FILE1 = 'UpdateAssetBundle.bat'
COPY_FILE2 = 'UpdateAssetBundle.sh'
BIND_CMD = 'git branch --set-upstream-to=origin/%s %s'

GIT_ADD_CMD = 'git add %s'
GIT_COMMIT_CMD = 'git commit -m "上传UpdateAssetBundle命令行文件[Auto Android]"'
GIT_PUSH_CMD = 'git push origin %s'

def copy_update_assetbudle_cmds():
    localutil.log("拷贝更新命令到指定目录")
    shutil.copyfile(COPY_SRC_PATH + COPY_FILE1,COPY_DEST_PATH + COPY_FILE1)
    shutil.copyfile(COPY_SRC_PATH + COPY_FILE2,COPY_DEST_PATH + COPY_FILE2)

def git_upload():
    localutil.log("开始执行上传文件")
    os.chdir(CD_ROOT)
    add_cmd = GIT_ADD_CMD % COPY_FILE1
    localutil.execute(add_cmd)
    add_cmd = GIT_ADD_CMD % COPY_FILE2
    localutil.execute(add_cmd)
    localutil.execute(GIT_COMMIT_CMD)
    push_cmd = GIT_PUSH_CMD % get_current_branch_name()
    localutil.execute(push_cmd)

#上传前需要保持到最新状态
def git_clean_and_update():
    localutil.log("开始执行清本地且更新")
    os.chdir(CD_ROOT)
    localutil.execute("git checkout .")
    localutil.execute("git clean -fd")
    branch_name = get_current_branch_name()
    bind_cmd = BIND_CMD % (branch_name,branch_name)
    localutil.execute(bind_cmd)
    localutil.execute("git pull")

def get_current_branch_name():
    os.chdir(CD_ROOT)
    archiveCmd = 'git branch'
    child1 = subprocess.Popen(archiveCmd, stdout=subprocess.PIPE)
    allinfo = child1.stdout.read().decode()
    split_datas = allinfo.split('\n')
    for split_data in split_datas:
        if len(split_data) == 0:
            continue
        if split_data[0] == '*':
            branch_name = split_data[2:len(split_data)]
            return branch_name

def main():
    git_clean_and_update()
    copy_update_assetbudle_cmds()
    git_upload()

if __name__ == "__main__":
    if localutil.check_disable():
        localutil.log("disable")
    else:
        main()
