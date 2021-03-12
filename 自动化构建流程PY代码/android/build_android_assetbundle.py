#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
# 作者: lhs
# 时间: 2021.02.22
# 用途: 编Android Assetbundle
#######################################################

import _thread
import time
import random
import os
import shutil
import datetime
import sys
import localutil
import compilerlog

#判定失败的时间 目前设定为30min
CHECK_FAIL_TIME = 60*30

#设置Unity3d项目目录
UNITY3D_PROJECT_PATH="G:/jenkinsworkspace/rex_client_android/rex_client"
#设置Unity3d执行的编译方法
UNITY3D_BUILD_METHOD="BuildingUtility.BuildAndroidAssetBundle"
#设置Unity3d exe文件路径
UNITY3D_EXE_PATH="C:/Program Files/Unity/Hub/Editor/2019.4.9f1/Editor/Unity.exe"

UNITY3D_OPEN_CMD = "\"" + UNITY3D_EXE_PATH + "\" -projectPath " + UNITY3D_PROJECT_PATH + " -quit -logFile unityLog.log"
UNITY3D_BUILDAB_CMD = "\"" + UNITY3D_EXE_PATH + "\" -projectPath " + UNITY3D_PROJECT_PATH + " -executeMethod " + UNITY3D_BUILD_METHOD + " -quit -logFile unityABLog.log"


allend = False
failEnd = False
openUnitySucc = False
openUnityFail = False

def childFunc(threadName, delay):
    global openUnityFail
    tick = 0
    while tick < CHECK_FAIL_TIME:
        time.sleep(1)
        tick+=1
        #如果打开Unity成功了，就不需要额外处理了
        if openUnitySucc:
            return
    #打开失败，杀死进程
    kill_unity()


def open_unity():
    localutil.log("open unity")
    if localutil.execute(UNITY3D_OPEN_CMD):
        localutil.log("Execute open cmd failed")

def unity_android_build_assetbundle():
    localutil.log("android build ab")
    if localutil.execute(UNITY3D_BUILDAB_CMD):
        localutil.log("Execute build ab cmd failed")

def mainFunc(threadName, delay):
    global openUnitySucc
    global openUnityFail
    global allend
    global failEnd
    compilerlog.set_prefix_path(UNITY3D_PROJECT_PATH + "/../")
    compilerlog.clear_open_log()
    open_unity()
    openUnitySucc = True
    #有打开的编译报错
    if compilerlog.check_open_log():
        failEnd = True
        return
    compilerlog.clear_compiler_log()
    unity_android_build_assetbundle()
    #有编AB包的编译报错
    if compilerlog.check_compile_log():
        failEnd = True
        return
    time.sleep(2)
    allend = True


def kill_unity():
    localutil.log("force kill unity")
    localutil.execute('taskkill /f /im unity.exe')

def copy_file():
    localutil.log("copy file")
    shutil.copyfile("G:/jenkinsworkspace/rex_client_android/Cmds/BuildConfig.json","G:/jenkinsworkspace/rex_client_android/rex_client/Tableex/BuildConfig.json")

def build():
    localutil.log("start build")
    # 创建两个线程
    try:
        _thread.start_new_thread( childFunc, ("Thread-1", 2, ) )
        _thread.start_new_thread( mainFunc, ("Thread-2", 4, ) )
    except:
        print("Error: unable to start thread")

    while (not allend) and (not failEnd):
        pass
    
    if failEnd:
        localutil.exit_fail()

if __name__ == '__main__':
    if(not localutil.check_disable()):
        build()
