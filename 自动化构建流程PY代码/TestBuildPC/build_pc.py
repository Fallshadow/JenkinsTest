#!/usr/bin/python
# -*- coding: UTF-8 -*-

import localutil
import localconfig
import compilerlog
import _thread
import time
import shutil

UNITY3D_COMPILE_CMD_FOR_PC = localconfig.UNITY3D_COMPILE_CMD_FOR_PC
# 判定失败的时间 目前设定为10min
CHECK_FAIL_TIME = 60 * 10

failEnd = False
allow = False
openUnitySucc = False
openUnityFail = False


def open_unity():
    localutil.log("open unity")
    if localutil.execute(localconfig.UNITY3D_OPEN_CMD):
        localutil.log("Execute open cmd failed")


def unity_compile():
    localutil.log("compile unity")
    if localutil.execute(UNITY3D_COMPILE_CMD_FOR_PC):
        localutil.log("Execute opne cmd failed")


def unity_buildab():
    localutil.log("build assetbundle")
    if localutil.execute(localconfig.UNITY3D_BUILDAB_CMD_FOR_PC):
        localutil.log("Execute compile cmd failed")


# 此项目的准备工作(此项目中需要更改build的设置、删除已经打包出来的残余文件/文件夹)
def prepareFunc():
    shutil.copyfile(localconfig.REX_TABLE_BYTE_FILE_ROOT, localconfig.REX_TABLE_BYTE_AUTO_FIX_FILE_ROOT)
    localutil.execute("for /d %a in (" + localconfig.GIT_PROJECT_PACK_PC_CD_ROOT + localconfig.GIT_PROJECT_COMPRESS_NAME + "*) do rd /s/q %a")


def mainFunc(delay):
    global openUnitySucc
    global openUnityFail
    global failEnd
    global allow
    compilerlog.set_prefix_path(localconfig.GIT_PROJECT_CD_ROOT + "/../")

    compilerlog.clear_open_log()
    open_unity()
    openUnitySucc = True
    # 有打开的报错
    if compilerlog.check_open_log():
        failEnd = True
        localutil.log("open error")
        return

    prepareFunc()

    compilerlog.clear_compiler_log()
    unity_buildab()
    unity_compile()
    if compilerlog.check_compiler_log():
        failEnd = True
        localutil.log("compiler error")
        return
    allow = True


def kill_unity():
    localutil.log("force kill unity")
    localutil.execute('taskkill /f /im unity.exe')


def childFunc(delay):
    global openUnityFail
    tick = 0
    while tick < CHECK_FAIL_TIME:
        time.sleep(delay)
        tick += delay
        # 如果打开Unity成功了，就不需要额外处理了
        if openUnitySucc:
            return
    # 打开失败，杀死进程
    kill_unity()


def build():
    localutil.log("start build")
    # 创建两个线程
    try:
        _thread.start_new_thread(childFunc, (2,))
        _thread.start_new_thread(mainFunc, (4,))
    except:
        localutil.log("Error: unable to start thread")

    while not allow and not failEnd:
        pass

    if failEnd:
        localutil.exit_fail()
        return
    localutil.log("build success")
    localutil.exit_success()


# 配置命令编译参数
def append_argv():
    global UNITY3D_COMPILE_CMD_FOR_PC
    append_args = localutil.get_current_argv_without_disable()
    UNITY3D_COMPILE_CMD_FOR_PC = UNITY3D_COMPILE_CMD_FOR_PC + append_args


if __name__ == '__main__':
    if localutil.check_disable():
        localutil.log("disable")
    else:
        append_argv()
        build()
