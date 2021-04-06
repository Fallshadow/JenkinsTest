#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 用途: 分析输出Unity编译报错日志
#######################################################

import os
import localutil

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


# 清除compilerlog文件
def clear_compiler_log():
    if os.path.exists(get_compile_log_path()):
        os.remove(get_compile_log_path())


# 检察是否有打开的错误
def check_open_log():
    if not os.path.exists(get_open_log_path()):
        return False
    f = open(get_open_log_path())
    have_error = False
    line = f.readline()
    while line:
        if line.find("error CS") != -1:
            if not have_error:
                localutil.log("================================Unity Open Error================================")
                have_error = True
            print(line)
        line = f.readline()
    if have_error:
        localutil.log("===========================================================================")
    f.close()
    return have_error


# 检察是否有编译的错误
def check_compiler_log():
    if not os.path.exists(get_compile_log_path()):
        return False
    f = open(get_compile_log_path())
    lines = f.read()
    f.close()
    localutil.log("================================Unity Error================================")
    print(lines)
    localutil.log("===========================================================================")
    compile_error = False

    if lines.find("[Exception]") != -1:
        compile_error = True

    if lines.find("error CS") != -1:
        compile_error = True
    return compile_error


def get_open_log():
    error_log = ''
    f = open(get_open_log_path())
    line = f.readline()
    while line:
        if line.find("error CS") != -1:
            error_log = error_log + line + "\n"
        line = f.readline()
    f.close()
    return error_log


def get_compile_log():
    error_log = ''
    f = open(get_compile_log_path())
    error_log = f.read()
    f.close()
    return error_log


def get_fail_log():
    exist_open_log = True
    exist_compile_log = True
    if not os.path.exists(get_open_log_path()):
        exist_open_log = False
    if not os.path.exists(get_compile_log_path()):
        exist_compile_log = False
    # 两个log都存在的时候，取最后修改的那份
    if exist_open_log and exist_compile_log:
        open_log = get_open_log()
        # open log中无相关阻断error信息
        if len(open_log) < 1:
            return get_compile_log()

        t1 = os.path.getmtime(get_open_log_path())
        t2 = os.path.getmtime(get_compile_log_path())
        if t1 > t2:
            return open_log
        else:
            return get_compile_log()

    if exist_open_log:
        return get_open_log()

    if exist_compile_log:
        return get_compile_log()

    return "Unknown Error"
