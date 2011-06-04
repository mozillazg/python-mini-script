import os

# os.path.getmtime(path) 
# os.path.basename(path)
# os.path.realpath(path)
# os.path.dirname(path) 
# os.rename(src, dst) 
# os.path.isdir(path) 
# os.path.isfile(path) 
# os.listdir(path)


    # if os.path.isfile(filepath):
    #   update_filename(filepath)
    # if os.path.isdir(filepath):
    #   file_paths(filepath)
    
    
# 遍历目录
def file_paths(dir_path):
    list_dirs = os.listdir(dir_path) # 获取给定目录下的文件及文件夹
    for dir in list_dirs:
        dir = os.path.realpath(dir_path + '/' + dir)
        print dir
        if os.path.isfile(dir):
            update_filename(dir)
        # if os.path.isdir(dir): # 如果是文件夹
            # file_paths(dir)  # 遍历子目录


def rename_file(file_path, old_filename, new_filename):
    os.rename(os.path.realpath(file_path), 
                        os.path.realpath(
                        os.path.dirname(file_path) # 文件所在目录的路径
                        +'/' + new_filename)
                    ) 


    date_modified = time.strftime('_%Y_%m_%d_%H_%M',
                                time.localtime(
                                os.path.getmtime(file_path)  # 文件最后修改时间
                                )) # 格式化日期
     
    file_basename = os.path.basename(file_path)
    
# 如果路径不存在
if not os.path.exists(save_path):
    # 创建用来保存图片的文件夹
    os.makedirs(save_path)   # os.mkdir(path) 不能创建多层目录，类似：a/b

os.renames(old, new) # 能创建多层目录，类似于移动并重命名文件的功能


os.walk  # 用来遍历目录

>>> for root, dir, file in os.walk('./'):
...     print file  # root： 目录路径，dir: 目录下的文件夹 ， file:目录下的文件
...
['movefile.py', 'sss']
['sss']

os.walk(top,topdown=False) # 先分析子目录
 
>>> for root, dir, file in os.walk('./'):
...     print file
...     dir[:] = []  # 只输出当前目录
...
['movefile.py', 'sss']

