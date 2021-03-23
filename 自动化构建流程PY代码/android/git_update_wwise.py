#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 作者: lhs
# 时间: 2021.02.22
# 用途: Git更新音效工程
#######################################################

import os
import localutil

GIT_URL = "http://10.15.120.11/root/rex_wwise.git"
GIT_BRANCH = "master"
CD_ROOT = "G:/jenkinsworkspace/rex_client_android/rex_client/rex_wwise"

def git_oper():
    localutil.execute('git config --global user.password "CP12cp12"')
    localutil.execute('git config --global user.name "clientpublish"')
    localutil.execute('git config credential.helper store')
    if os.path.exists(".git"):
        localutil.execute("git reset --hard")
        localutil.execute("git clean -fd")
        localutil.execute("git pull origin " + GIT_BRANCH)
    else:
        localutil.execute("git init")
        localutil.execute("git remote add -f origin " + GIT_URL)
        localutil.execute("git config core.sparsecheckout true")
        localutil.execute("git pull origin " + GIT_BRANCH)
    localutil.execute("git fetch --all")
    localutil.execute("git reset --hard origin/" + GIT_BRANCH)
    localutil.execute("git checkout " + GIT_BRANCH)

def main():
    localutil.log("Start git update")
    if not os.path.exists(CD_ROOT):
        os.makedirs(CD_ROOT)
    os.chdir(CD_ROOT)
    git_oper()
    localutil.log("End git update")

if __name__ == "__main__":
    if localutil.check_disable():
        localutil.log("disable")
    else:
        main()


