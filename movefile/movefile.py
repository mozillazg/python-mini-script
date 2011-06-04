#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""移动文件到相应日期目录下。
例如：test.txt 最后修改时间：2011/06/03
移动到目录 2011/06 下
"""

import os
import time

#生成器
def file_paths(dir_path):
    """生成器-查找目录下的文件
    """
    for root, dirs, files in os.walk(dir_path):
        dirs[:] = [] # 忽略子目录
        for f in files:
            yield os.path.join(root, f)

def move_file(file_path):
    """移动文件到相应的日期目录下
    """
    if os.path.isdir(file_path):
        for f in file_paths(file_path):
            move_file(f)
    elif  os.path.isfile(file_path):
        date_time  = time.strftime('%Y/%m',time.localtime(
                 os.path.getmtime(file_path)  # 文件最后修改时间
                 ))
        dirname = os.path.dirname(file_path)
        basename = os.path.basename(file_path)
        new_filepath = os.path.join(dirname, date_time, basename)
        os.renames(file_path, new_filepath)

def main():
    filepath = raw_input("please input the file or dir path:")
    move_file(filepath)

if __name__ == '__main__':
    main()
