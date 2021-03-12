#!/usr/bin/python
# -*- coding: UTF-8 -*-

import localutil
import localconfig
import compilerlog

UNITY3D_OPEN_CMD = "\"" + localconfig.UNITY3D_EXE_PATH + "\" -projectPath " + localconfig.UNITY3D_PROJECT_PATH + " -quit -logFile unityOpenLog.log"
UNITY3D_COMPILE_CMD = "\"" + localconfig.UNITY3D_EXE_PATH + "\" -projectPath " + localconfig.UNITY3D_PROJECT_PATH + " -executeMethod " + localconfig.UNITY3D_BUILD_METHOD + " -quit -logFile unityCompileLog.log"

# 判定失败的时间 目前设定为30min
CHECK_FAIL_TIME = 60*30

openUnitySucc = False
openUnityFail = False

def open_unity():
	localutil.log("open unity")
	if localutil.execute(UNITY3D_OPEN_CMD):
		localutil.log("Execute open cmd failed")


def mainFunc(delay):
	global openUnitySucc
	global openUnityFail
    compilerlog.set_prefix_path(localconfig.UNITY3D_PROJECT_PATH + "/../")
    compilerlog.clear_open_log()
    open_unity()


def kill_unity():
	localutil.log("force kill unity")
	localutil.execute('taskkill /f /im unity.exe')


def childFunc(delay):
	global openUnityFail
	tick = 0
	while tick < CHECK_FAIL_TIME:
		time.sleep(delay)
		tick+=delay
		# 如果打开Unity成功了，就不需要额外处理了
		if openUnitySucc:
			return
	# 打开失败，杀死进程
	kill_unity()


def build():
	localutil.log("start build")
	# 创建两个线程
	try:
		_thread.start_new_thread( childFunc, (2) )
		_thread.start_new_thread( mainFunc, (4) )
	except:
		localutil.log("Error: unable to start thread")

    while (not allend) and (not failEnd):
        pass

    if failEnd:
        localutil.exit_fail()


# 配置命令编译参数
def append_argv():
    global UNITY3D_COMPILE_CMD
    append_args = localutil.get_current_argv_without_disable()
    UNITY3D_COMPILE_CMD = UNITY3D_COMPILE_CMD + append_args


if __name__ == '__main__':
	if localutil.check_disable():
		localutil.log("disable")
	else:
        append_argv()
		build()