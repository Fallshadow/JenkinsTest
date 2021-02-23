"""
打包模块：git相关工作
"""

# -*- coding: utf-8 -*-

import os
import sys
import subprocess

'''
全局变量：有关git的信息
'''

# git url
GIT_URL = "https://github.com/Fallshadow/JenkinsTest.git"
# git项目路径
CD_ROOT = "D:/Project/JenkinsTest"
# git log 输出目录
CD_GIT_LOG_PRINT_TXT = "D:/Project/GitLogText.txt"
# git预打包分支
GIT_BRANCH = "main"


def check_argv_git_branch():
    global GIT_BRANCH
    if len(sys.argv) >= 3:
        GIT_BRANCH = sys.argv[2]
        log("切换到git分支:" + sys.argv[2])


def check_argv_disable():
    is_disable = False
    if len(sys.argv) >= 2:
        if sys.argv[1] == "disable" or sys.argv[1] == "Disable":
            is_disable = True
    log("是否开启此PY is_disable : %s" % is_disable)
    return is_disable


def git_log_text(git_infos):
    log_file = open(CD_GIT_LOG_PRINT_TXT, 'w', encoding='utf8')
    log_file.write(git_infos)
    log_file.close()


'''
两个log集合进行差异输出
'''


def git_diff_log(git_info_before, git_info_after):
    diff_log_hash = set()
    for git_info in git_info_before:
        diff_log_hash.add(git_info[0])
    print("==========================================================================================")
    index = 1
    git_logs = ' '
    for git_info in git_info_after:
        if git_info[0] not in diff_log_hash:
            desc_info = ' '
            for item in git_info[1]:
                desc_info = desc_info + " " + item
            print("[" + str(index) + "]" + desc_info)
            git_logs = git_logs + desc_info + '\n'
            index = index + 1
    print("==========================================================================================")
    git_log_text(git_logs)


'''
针对每一条git log信息，每一个子列表以 哈希、详细信息 的形式存在列表里
'''


def git_log():
    git_cmd_log = 'git log --since="1 weeks ago" --pretty=format:"%H %s %cn" --no-merges'
    subprocess1 = subprocess.Popen(git_cmd_log, stdout=subprocess.PIPE)
    git_infos_str = subprocess1.stdout.read().decode()
    git_infos_list = git_infos_str.split('\n')
    git_log_list_desc_list = []
    for git_infos_item in git_infos_list:
        git_infos_item_list = git_infos_item.split(' ')
        git_hash = git_infos_item_list[0]
        git_desc = git_infos_item_list[1:len(git_infos_item_list)]
        git_infos_desc_list = [git_hash, git_desc]
        git_log_list_desc_list.append(git_infos_desc_list)
    return git_log_list_desc_list


def git_update():
    exec_cmd('git checkout .')
    exec_cmd('git clean -df')
    exec_cmd('git reset --hard HEAD^')
    exec_cmd('git remote set-url origin ' + GIT_URL)
    exec_cmd('git checkout -b ' + GIT_BRANCH + ' origin/' + GIT_BRANCH)
    exec_cmd('git checkout ' + GIT_BRANCH)
    exec_cmd('git pull')


'''
进行git配置
上传的用户名、永久显式保存用户名密码、大小写敏感
'''


def git_config():
    exec_cmd('git config --global user.name "packPC"')
    exec_cmd('git config --global user.password "packPC"')
    exec_cmd('git config credential.helper store')
    exec_cmd('git config --global core.ignorecase false')


def log(message):
    print("[log] " + message)


def exec_cmd(cmd):
    log("execute cmd >> " + cmd)
    os.system(cmd)


def main():
    log("start git update")
    os.chdir(CD_ROOT)
    git_config()
    git_infos_before = git_log()
    git_update()
    git_infos_after = git_log()
    git_diff_log(git_infos_before, git_infos_after)
    log("end git update")


def log_argv():
    index = 0
    for item in sys.argv:
        log("[" + str(index) + "]" + item + " ")
        index = index + 1


if __name__ == "__main__":
    log("准备执行git更新相关")
    log_argv()
    if not check_argv_disable():
        check_argv_git_branch()
        main()
