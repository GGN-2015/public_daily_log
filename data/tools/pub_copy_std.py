import pub_dir_utils

def copy_std(): # 从日常生活规范项目拷贝一个 README.md 过来
    filefrom = pub_dir_utils.get_std_readme_dir()
    fileto   = pub_dir_utils.get_root_dir("data", "auto-gen", "life-standard.md")
    content  = open(filefrom, "r", encoding="utf-8").read()
    open(fileto, "w", encoding="utf-8").write(content)

if __name__ == "__main__":
    copy_std()