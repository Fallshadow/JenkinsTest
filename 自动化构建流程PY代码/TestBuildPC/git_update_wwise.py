#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import sys
import localutil
import localconfig

# git url
GIT_URL = localconfig.GIT_WWISE_URL
# git项目路径
CD_ROOT = localconfig.GIT_WWISE_CD_ROOT
# git log 输出目录
CD_GIT_LOG_PRINT_TXT = localconfig.GIT_WWISE_LOG_CD_TXT
# git预打包分支
GIT_BRANCH = localconfig.GIT_WWISE_BRANCH


def main():
    localutil.log("Start git update")
    if not os.path.exists(localconfig.GIT_WWISE_CD_ROOT):
        os.makedirs(localconfig.GIT_WWISE_CD_ROOT)
    os.chdir(localconfig.GIT_WWISE_CD_ROOT)
    localutil.git_config()
    localutil.git_update(GIT_URL, GIT_BRANCH)
    localutil.log("End git update")


# 打印参数 第一个参数（index = 1）为disable 第二个参数为切换的分支
def log_argv():
    index = 0
    for item in sys.argv:
        localutil.log("[" + str(index) + "]" + item + " ")
        index = index + 1


# 切换到git分支
def check_argv_git_branch():
    global GIT_BRANCH
    if len(sys.argv) >= 3:
        GIT_BRANCH = sys.argv[2]
        localutil.log("准备切换到git分支:" + sys.argv[2])


if __name__ == "__main__":
    localutil.log("准备执行音效项目git更新相关")
    log_argv()
    if not localutil.check_disable():
        check_argv_git_branch()
        main()


