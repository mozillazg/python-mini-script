#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""移动文件夹到相应日期目录下。
例如：test.txt 创建于：2011/06/03
移动到目录 2011/06 下
"""

import os
import time

# 遍历目录
def file_paths(dir_path):
    """遍历整个目录,并对目录下的文件进行操作
    """
    list_dirs = os.listdir(dir_path) # 获取给定目录下的文件及文件夹
    for dir in list_dirs:
        dir = os.path.realpath(dir_path + '/' + dir)
        if os.path.isfile(dir):
            move_file(dir)

def move_file(file_path):
    """移动文件到相应的日期目录下
    """
    date_time  = time.strftime('%Y/%m',time.localtime(
                 os.path.getctime(file_path)  # 文件创建时间
                 ))
    basename = os.path.basename(file_path)
    dirpath = os.path.realpath(os.path.dirname(file_path) + '/' + date_time)
    new_filepath = os.path.realpath(dirpath+'/'+basename)
    #if not os.path.exists(dirpath):
        #os.makedirs(dirpath)
    #os.system(' move "%s" "%s" ' % (file_path, new_filepath))
    os.renames(file_path, new_filepath)

def main():
    filepath = raw_input("please input the file or dir path:")
    if os.path.isfile(filepath):
        move_file(filepath)
    if os.path.isdir(filepath):
        file_paths(filepath)

if __name__ == '__main__':
    main()
