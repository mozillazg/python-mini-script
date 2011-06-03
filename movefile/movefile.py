#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""移动文件夹到相应日期目录下。
例如：test.txt 创建于：2011/06/03
移动到目录 2011/06 下
"""

import os
import time

#生成器
def file_paths(dir_path):
    """生成器-查找目录下的文件
    """
    list_dirs = os.listdir(dir_path) # 获取给定目录下的文件及文件夹
    for  f in list_dirs:
        f = os.path.realpath(dir_path + '/' + f)
        if os.path.isfile(f):
            yield f

def move_file(file_path):
    """移动文件到相应的日期目录下
    """
    if os.path.isdir(file_path):
        for f in file_paths(file_path):
            move_file(f)
    elif  os.path.isfile(file_path):
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
    move_file(filepath)

if __name__ == '__main__':
    main()
