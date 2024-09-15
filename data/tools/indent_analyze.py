def get_indent_len(content) -> int:
    if content.lstrip().startswith("-"):
        return 2
    else:
        return 3

def get_indent_degree(line_content: str): # 分析缩进等级或者标题等级
    if line_content.lstrip().startswith("#"):
        return "H" + str(len(line_content.split()[0]))
    elif line_content.lstrip()[0].isdigit() or line_content.lstrip()[0] == "-":
        indent_len = get_indent_len(line_content)
        indent_cnt = (len(line_content) - len(line_content.lstrip()))
        assert indent_cnt % indent_len == 0 # 要保证整除
        return "C" + str(indent_cnt // indent_len)
    else:
        return "CX"

def get_all_lines_in_markdown(filename):
    lines = open(filename, "r", encoding="utf-8").read().split("\n")
    lines = [
        (
            get_indent_degree(x.rstrip()), # 等级
            x.strip()                      # 内容
        )
        for x in lines
        if x.rstrip() != "" # 获得所有非空行
    ]
    return lines

if __name__ == "__main__":
    for line in (get_all_lines_in_markdown("README.md")):
        print(line)