#!/usr/bin/python
# -*- coding: UTF-8 -*-

import localconfig
import localutil


def param_test():
    localutil.log(localconfig.BUILD_TIMESTAMP)


if __name__ == '__main__':
    if localutil.check_disable():
        localutil.log("disable")
    else:
        param_test()
        # shutil.copyfile("D:/Test/act_pc_2021-04-06-09-52-19.rar", "D:/Test/mytest/mytest.rar")
