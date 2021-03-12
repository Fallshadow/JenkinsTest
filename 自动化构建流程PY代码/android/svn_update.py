#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 作者: lhs
# 时间: 2021.02.22
# 用途: SVN更新
# 暂时先废弃吧
#######################################################

import os
import sys
import shutil

DEST_PATH = "G:/jenkinsworkspace/rex_client_android/rex_client/Android/"
SRC_PATH = "D:/act_assetbundle_ex/trunk/Android/"

CD_ROOT = "D:/act_assetbundle_ex/trunk"
SVN_UPDATE = 'svn update'
DEST_PATH = "G:/jenkinsworkspace/rex_client_android/rex_client/Assetbundle/Android/"

def log(msg):
    print("[Log]" + msg)

def execute(cmd):
    log("execute cmd >> " + cmd)
    os.system(cmd)

def copy_files():
    #先删除原有数据目录
    log("开始删除原有Assetbundle数据")
    if os.path.exists(DEST_PATH):
        shutil.rmtree(DEST_PATH)
    #再把新的数据拷贝过去
    log("开始从trunk拷贝数据")
    shutil.copytree(SRC_PATH, DEST_PATH)

def svn_update():
    log("先svn的trunk更到最新")
    os.chdir(CD_ROOT)
    execute(SVN_UPDATE)

def main():
    svn_update()
    copy_files()

if __name__ == "__main__":
    main()
