#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 用途: 分析输出Unity编译报错日志
#######################################################

import os
import shutil
import localutil
import sys

Prefix_Path = ""


def set_prefix_path(path):
    global Prefix_Path
    Prefix_Path = path


def get_open_log_path():
    return Prefix_Path + "unityOpenLog.log"


def get_compile_log_path():
    return Prefix_Path + "unityCompileLog.log"


# 清除openlog文件
def clear_open_log():
    if os.path.exists(get_open_log_path()):
        os.remove(get_open_log_path())


def clear_compiler_log():
    if os.path.exists(get_compile_log_path()):
        os.remove(get_compile_log_path())