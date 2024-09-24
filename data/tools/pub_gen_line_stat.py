# 生成行数统计信息
import pub_git_utils
import pub_dir_utils

def gen_line_stat_file():
    filepath = pub_dir_utils.get_root_dir("data", "auto-gen", "line-stat.md")
    content  = pub_git_utils.gen_line_stat_content()
    open(filepath, "w", encoding="utf-8").write(content)

if __name__ == "__main__":
    gen_line_stat_file()