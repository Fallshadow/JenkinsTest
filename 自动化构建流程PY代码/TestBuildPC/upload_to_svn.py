#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import time
import subprocess
import localutil

CD_ROOT = 'D:/act_assetbundle_ex/trunk'
SVN_UPDATE = 'svn update'
SVN_STATUS_COMMAD = 'svn status'
SVN_INFO = 'svn info'

# 最新ab包地址
SRC_PATH = 'G:/jenkinsworkspace/rex_client_android/rex_client/Assetbundle/Android'
# svn ab包地址
DEST_PATH = 'D:/act_assetbundle_ex/trunk/Android'

# svn的各种指令
SVN_DELETE_ORIGIN = 'svn delete %s'
SVN_ADD_ORIGIN = 'svn add %s'
SVN_COMMIT_TRUNK = 'svn commit -m "commit assetbundle"'

BAT_CONTENT = '''echo "开始删除旧的AssetBundle"
rd /s /Q Assetbundle
echo "开始下载新的AssetBundle"
svn export -r %s https://10.15.120.11:18080/svn/act_assetbundle_ex/trunk Assetbundle
echo "结束！"
pause'''

SH_CONTENT = '''echo "开始删除旧的AssetBundle"
rm -rf Assetbundle
echo "开始下载新的AssetBundle"
svn export -r %s https://10.15.120.11:18080/svn/act_assetbundle_ex/trunk Assetbundle
echo "结束！"'''

CMD_FILE_PATH = 'G:/jenkinsworkspace/rex_client_android/tempdata/'
BAT_FILE_NAME = CMD_FILE_PATH + 'UpdateAssetBundle.bat'
SH_FILE_NAME = CMD_FILE_PATH + 'UpdateAssetBundle.sh'


# svn更新
def svn_update():
    localutil.log("先svn的trunk更到最新")
    os.chdir(CD_ROOT)
    localutil.execute(SVN_UPDATE)


def copy_files():
    # 先删除原有数据目录
    localutil.log("开始删除原有trunk数据")
    if os.path.exists(DEST_PATH):
        shutil.rmtree(DEST_PATH)
    # 再把新的数据拷贝过去
    localutil.log("开始拷贝数据到trunk")
    shutil.copytree(SRC_PATH, DEST_PATH)


# 收集命令信息
def collect_cmd_output(cmd):
    child1 = subprocess.Popen(cmd, stdout=subprocess.PIPE,)
    allinfo = child1.stdout.read().decode(errors='ignore')
    return allinfo


def generate_svn_commit_all_cmd(svn_status):
    split_datas = svn_status.split('\n')
    add_list = []
    delete_list = []
    for item in split_datas:
        item_len = len(item)
        if item_len != 0:
            if item[0] == '?':
                add_item = SVN_ADD_ORIGIN % item[8:item_len]
                add_list.append(add_item)
            elif item[0] == '!':
                delete_item = SVN_DELETE_ORIGIN % item[8:item_len]
                delete_list.append(delete_item)
    return [add_list, delete_list]


def svn_upload_trunk():
    os.chdir(CD_ROOT)
    svn_status = collect_cmd_output(SVN_STATUS_COMMAD)
    cmds = generate_svn_commit_all_cmd(svn_status)
    # 执行删除
    for cmd_item in cmds[1]:
        localutil.execute(cmd_item)
    # 执行添加
    for cmd_item in cmds[0]:
        localutil.execute(cmd_item)
    # 执行commit
    localutil.execute(SVN_COMMIT_TRUNK)


# 生成bat文件，用于下载指定tag的AssetBundle文件
def generate_cmd_files(time_version):
    localutil.log("开始生成bat文件")
    f = open(BAT_FILE_NAME, 'w')
    write_content = BAT_CONTENT % time_version
    f.write(write_content)
    f.close()
    localutil.log("开始生成sh文件")
    f = open(SH_FILE_NAME, 'w')
    write_content = SH_CONTENT % time_version
    f.write(write_content)
    f.close()


def get_version():
    time_version = time.strftime("%Y%m%d.%H%M%S",time.localtime())
    return time_version


def get_svn_revision():
    os.chdir(CD_ROOT)
    infos = collect_cmd_output(SVN_INFO)
    localutil.log(infos)
    split_datas = infos.split('\n')
    for item in split_datas:
        if item.startswith('Revision'):
            return item[10:len(item)]


def main():
    svn_update()
    # 拷贝新生成的ab到svn目录
    copy_files()
    # svn上传
    svn_upload_trunk()
    svn_update()
    svn_version = get_svn_revision()
    int_version = int(svn_version)
    str_version = str(int_version)
    # 生成bat和sh
    generate_cmd_files(str_version)


if __name__ == "__main__":
    if not localutil.check_disable():
        main()
