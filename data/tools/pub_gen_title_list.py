# 生成名字索引
import pub_dir_utils
import pub_mylog
import os

def get_title_from_markdown(filepath): # 获取标题栏信息
    content = open(filepath, "r", encoding="utf-8").read().strip().split("\n")
    if len(content) == 0 or len(content[0]) == 0:
        pub_mylog.log("- <<1;33[WARN]>>: file `<<1;33[%s]>>` has empty title line." % filepath)
        return
    if not content[0].startswith("# "):
        pub_mylog.log("- <<1;31[ERROR]>>: file `<<1;33[%s]>>` does not has a title." % filepath)
        assert False
    return content[0][1:].strip()

def get_all_path_title_pair() -> list: # 获得所有文章的标题
    pair_list = []
    for file in pub_dir_utils.get_all_markdown_file():
        title_now = (get_title_from_markdown(file))
        pair_list.append((pub_dir_utils.get_project_dir_list(file), title_now))
    return sorted(pair_list, key=lambda x: x[1])

def gen_link(path_list) -> str:
    real_path = os.path.join("..", "..", *path_list)
    return "[%s](%s)" % (path_list[-1], real_path)

def gen_title_list_content(): # 创建自动生成的标题索引文件
    content  = "# 《`GGN_2015` 公开日志的标题索引》\n"
    content += "| 标题 | 链接 |\n"
    content += "| ---- | ---- |\n"
    for path_list, title in get_all_path_title_pair():
        content += "| %s | %s |\n" % (title, gen_link(path_list))
    return content

def create_title_list_file():
    filepath = pub_dir_utils.get_root_dir("data", "auto-gen", "title-list.md")
    try:
        os.remove(filepath) # 一定要先删除原有文件
    except:
        pass
    content = gen_title_list_content()
    pub_mylog.log("- <<1;32[INFO]>>: generating title list file ...")
    open(filepath, "w", encoding="utf-8").write(content)

if __name__ == "__main__":
    create_title_list_file()