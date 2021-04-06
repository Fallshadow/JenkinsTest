#!/usr/bin/python
# -*- coding: UTF-8 -*-

import localutil
import localconfig
import shutil
import datetime
import subprocess


def main():
    localutil.log("开始压缩复制文件")
    localutil.execute("C:/Windows/Rar.exe a -ag" + localconfig.BUILD_TIMESTAMP + " -ep1 -df -m1 "
                      + localconfig.SRC_EXE_PATH
                      + localconfig.GIT_PROJECT_COMPRESS_NAME
                      + " "
                      + localconfig.GIT_PROJECT_PACK_PC_CD_ROOT
                      + localconfig.GIT_PROJECT_COMPRESS_NAME
                      + "*/")
    # 上面一步到位
    # shutil.copyfile(localconfig.GIT_PROJECT_PACK_PC_CD_ROOT + localconfig.GIT_PROJECT_COMPRESS_NAME + localconfig.BUILD_TIMESTAMP + ".rar",
    #                localconfig.SRC_EXE_PATH + localconfig.GIT_PROJECT_COMPRESS_NAME + localconfig.BUILD_TIMESTAMP + ".rar")
    localutil.log("结束压缩复制文件")


if __name__ == '__main__':
    if localutil.check_disable():
        localutil.log("disable")
    else:
        main()
