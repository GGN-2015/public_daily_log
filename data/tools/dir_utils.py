import os
import functools

def get_tools_dir():
    return os.path.dirname(os.path.abspath(__file__))

def get_root_dir():
    return os.path.dirname(get_tools_dir())

def __get_dir_filelist(dirpath) -> list: # 获取某个目录中的所有文件
    return os.listdir(dirpath)

def __get_dir_filelist_recursive(dirpath): # 递归获取目录树中的所有文件
    dirpath = os.path.abspath(dirpath)
    arr = []
    for filename in __get_dir_filelist(dirpath):
        filepath = os.path.join(dirpath, filename)
        if os.path.isdir(filepath):
            arr += __get_dir_filelist_recursive(filepath)
        else:
            arr += [filepath]
    return sorted(arr)

def __get_path_split(path_content): # 拆分文件名
    l, r = os.path.split(path_content)
    if l == path_content or r == path_content:
        return [path_content]
    else:
        return [ # 删除空目录
            x 
            for x in (__get_path_split(l) + __get_path_split(r))
            if x != ""
        ]

@functools.cache
def get_all_file_in_this_project(): # 忽略 .git 文件夹
    arr = []
    root_dir  = get_root_dir()
    file_list = __get_dir_filelist_recursive(root_dir)
    for file in file_list:
        relpath = os.path.relpath(file, root_dir)
        if __get_path_split(relpath)[0] != ".git":
            arr.append(file)
    return arr

if __name__ == "__main__":
    for file in get_all_file_in_this_project():
        print(file)