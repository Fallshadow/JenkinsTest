#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# 项目的 git url
GIT_PROJECT_URL = "https://github.com/Fallshadow/JenkinsTest.git"
# 项目的 git预打包分支
GIT_PROJECT_BRANCH = "main"
# 项目的 git路径
GIT_PROJECT_CD_ROOT = "D:/Project/JenkinsTest2"
# 项目的 git log 输出目录
GIT_PROJECT_LOG_CD_TXT = "D:/Project/JenkinsTest2/GitLogText.txt"
# 项目的 预打包路径
GIT_PROJECT_PACK_PC_CD_ROOT = "D:/Project/"
# 项目的 压缩头名称
GIT_PROJECT_COMPRESS_NAME = "ACT_PC_"

# 音效项目的 git url
GIT_WWISE_URL = "http://10.15.120.11/root/rex_wwise.git"
# 音效项目的 git预打包分支
GIT_WWISE_BRANCH = "master"
# 音效项目的 git路径
GIT_WWISE_CD_ROOT = "G:/jenkinsworkspace/rex_client_android/rex_client/rex_wwise"
# 音效项目的 git log 输出目录
GIT_WWISE_LOG_CD_TXT = "D:/Project/GitLogText.txt"

# PC版本设置Unity3d执行的编译方法
UNITY3D_BUILD_METHOD_FOR_PC = "BuildingUtility.BuildWindows"
UNITY3D_BUILDAB_METHOD_FOR_PC = "BuildingUtility.BuildWindowsAB"

# 设置Unity3d exe文件路径
UNITY3D_EXE_PATH = "D:/Rex_editor/Editor/Unity.exe"
UNITY3D_OPEN_CMD = UNITY3D_EXE_PATH + " -projectPath " + GIT_PROJECT_CD_ROOT + " -quit -logFile unityOpenLog.log"
UNITY3D_BUILDAB_CMD_FOR_PC = UNITY3D_EXE_PATH + " -projectPath " + GIT_PROJECT_CD_ROOT + " -executeMethod " + UNITY3D_BUILDAB_METHOD_FOR_PC + " -quit -logFile unityABLog.log"
UNITY3D_COMPILE_CMD_FOR_PC = UNITY3D_EXE_PATH + " -projectPath " + GIT_PROJECT_CD_ROOT + " -executeMethod " + UNITY3D_BUILD_METHOD_FOR_PC + " -quit -logFile unityCompileLog.log"

# PC版本打包出来的最终路径
SRC_EXE_PATH = "D:/JenkinsWorkspace/"

# PC版本ftp的相关设置
FTP_IP = "10.15.120.85"
FTP_PORT = 21
FTP_USERNAME = "ssc"
FTP_PASSWORD = "12345678"
FTP_EXE_PATH = "/client_pkg/rex/pc/"

# jenkins打包参数
LOCAL_BUILD_TIMESTAMP_STR = ""
BUILD_TIMESTAMP = os.getenv("BUILD_TIMESTAMP")

# 特殊項目的一些特殊操作
REX_TABLE_BYTE_FILE_ROOT = "C:/rex_client/Tableex/BuildConfig.json"
REX_TABLE_BYTE_AUTO_FIX_FILE_ROOT = "C:/Users/JenkinsAutoForPC/BuildConfig.json"
