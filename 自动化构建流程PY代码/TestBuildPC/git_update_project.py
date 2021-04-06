# -*- coding: utf-8 -*-

import os
import sys
import localutil
import localconfig


# git url
GIT_URL = localconfig.GIT_PROJECT_URL
# git项目路径
CD_ROOT = localconfig.GIT_PROJECT_CD_ROOT
# git log 输出目录
CD_GIT_LOG_PRINT_TXT = localconfig.GIT_PROJECT_LOG_CD_TXT
# git预打包分支
GIT_BRANCH = localconfig.GIT_PROJECT_BRANCH


# 切换到git分支
def check_argv_git_branch():
    global GIT_BRANCH
    if len(sys.argv) >= 3:
        GIT_BRANCH = sys.argv[2]
        localutil.log("准备切换到git分支:" + sys.argv[2])


def main():
    localutil.log("start git update")
    os.chdir(CD_ROOT)
    localutil.git_config()
    git_infos_before = localutil.git_log()
    localutil.git_update(GIT_URL, GIT_BRANCH)
    git_infos_after = localutil.git_log()
    localutil.git_diff_log(git_infos_before, git_infos_after, CD_GIT_LOG_PRINT_TXT)
    localutil.log("end git update")


# 打印参数 第一个参数（index = 1）为disable 第二个参数为切换的分支
def log_argv():
    index = 0
    for item in sys.argv:
        localutil.log("[" + str(index) + "]" + item + " ")
        index = index + 1


if __name__ == "__main__":
    localutil.log("准备执行项目git更新相关")
    log_argv()
    if not localutil.check_disable():
        check_argv_git_branch()
        main()
