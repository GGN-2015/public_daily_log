import os
import functools

def get_tools_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))

def get_root_dir(*args) -> str:
    base = os.path.dirname(os.path.dirname(get_tools_dir()))
    return os.path.join(base, *args)

def get_readme_filepath() -> str:
    return os.path.join(get_root_dir(), "README.md")

def get_github_dir() -> str:
    return os.path.dirname(get_root_dir())

def get_std_dir() -> str:
    return os.path.join(get_github_dir(), "life_standard")

def get_std_readme_dir() -> str:
    return os.path.join(get_std_dir(), "README.md")

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
def get_all_file_in_this_project(): # 忽略 .git 文件夹以及 .pyc 文件
    arr = []
    root_dir  = get_root_dir()
    file_list = __get_dir_filelist_recursive(root_dir)
    for file in file_list:
        relpath = os.path.relpath(file, root_dir)
        if __get_path_split(relpath)[0] != ".git" and not file.endswith(".pyc"):
            arr.append(file)
    return arr

def split_filename(filename) -> list: # 拆分路径
    l, r = os.path.split(filename)
    if l == filename or r == filename:
        return [filename]
    else:
        return split_filename(l) + split_filename(r)

def get_project_dir_list(filepath): # 路径拆分
    return split_filename(os.path.relpath(filepath, get_root_dir()))

def get_all_relpath_in_this_project():
    arr = []
    for file in get_all_file_in_this_project():
        arr.append(get_project_dir_list(file))
    return arr

def get_all_markdown_file(): # 获取项目中的所有 markdown 文件
    return [
        x
        for x in get_all_file_in_this_project()
        if x.endswith(".md")
    ]

if __name__ == "__main__":
    for file in get_all_relpath_in_this_project():
        print(file)