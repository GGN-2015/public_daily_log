# 生成名字索引
import pub_dir_utils

def get_title_from_markdown(filepath): # 获取标题栏信息
    content = open(filepath, "r", encoding="utf-8").read().strip().split("\n")
    assert content[0].startswith("# ")
    return content[0][1:].strip()

if __name__ == "__main__":
    for file in pub_dir_utils.get_all_markdown_file():
        print(get_title_from_markdown(file))