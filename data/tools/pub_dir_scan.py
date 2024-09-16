import pub_dir_utils

def get_all_markdown_file(): # 获取项目中的所有 markdown 文件
    return [
        x
        for x in pub_dir_utils.get_all_file_in_this_project()
        if x.endswith(".md")
    ]

if __name__ == "__main__":
    for x in (get_all_markdown_file()):
        print(x)