import markdown2
import re
import pub_dir_utils
import pub_mylog
import base64
import string
import secrets

def generate_random_sequence(length): 
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits # 定义字符集，包括小写字母、大写字母和数字
    random_sequence = ''.join(secrets.choice(characters) for _ in range(length)) # 使用 secrets.choice 来生成随机序列
    return random_sequence

def pre_scan(content: str) -> str: # 有些行前面有必须要删除的先导空格，会影响标题的识别
    new_content = ""
    for line in content.split("\n"):
        if line.lstrip().startswith("#"):
            new_content += line.lstrip() + "\n"
        else:
            new_content += line + "\n"
    return new_content

# 中介常量：必须是随机的字母数字序列
RAW_DOLLAR         = generate_random_sequence(64)
MATH_CONTENT_BEGIN = generate_random_sequence(64)
MATH_CONTENT_END   = generate_random_sequence(64)
HTML_LINK_BEGIN    = generate_random_sequence(64)
HTML_LINK_END      = generate_random_sequence(64)

CDN = """
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
"""

# 用于生成指定 markdown 文件的 html 版本
def get_html_from_md(md_text):
    html = markdown2.markdown(md_text, extras=['mathjax', "fenced-code-blocks", "code-friendly", 'tables'])
    html_with_mathjax = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        .math {{
            display: block;
            overflow-wrap: break-word;
        }}

        /* 当屏幕宽度大于高度时 */
        @media (orientation: landscape) {{
            .math-container, body {{
                max-width: 640px;
                margin: 0 auto;
            }}

            pre, img {{
                max-width: 640px;
            }}
        }}

        /* 其他样式 - 默认竖屏 */
        @media (orientation: portrait) {{
            .math-container, body {{
                max-width: 1080px;
                margin: 0 auto;
                font-size: 48px;
            }}

            pre, img {{
                max-width: 1080px;
            }}
        }}
    </style>
    {CDN}
</head>
<body>
    {html}
</body>
</html>
    """
    return html_with_mathjax

# 封装 http 和 https 链接
# 一定要考虑一件事：较短的链接可能是某个较长链接的前缀，因此替换时候一定要考虑到先替换长的才是正确的做法
def wrap_http_link(md_text):
    regex = r"[^\[\(]{1}(http(s)?://[^\s\n]+)[\s\n]{1}"
    new_text = md_text
    action_pair_list = []
    for match in re.finditer(regex, md_text):
        old_link = match.group(1)
        new_link = HTML_LINK_BEGIN + base64.b64encode(old_link.encode("utf-8")).decode("utf-8") + HTML_LINK_END
        action_pair_list.append((old_link, new_link))
    action_pair_list = sorted(action_pair_list, key=lambda x:-len(x[0])) # 一定要先替换长的
    for old_link, new_link in action_pair_list:
        new_text = new_text.replace(old_link, new_link)
    return new_text

# 把数学块内容保护起来
def wrap_math_content(md_text):
    regex = r"\$+[^\$]+\$+"
    new_text = md_text
    for match in re.finditer(regex, md_text):
        old_link = match.group(0)
        new_link = MATH_CONTENT_BEGIN + base64.b64encode(old_link.encode("utf-8")).decode("utf-8") + MATH_CONTENT_END
        new_text = new_text.replace(old_link, new_link)
    return new_text

# 将指向 markdown 文件的链接改为指向 html 文件的
def rename_link(md_text): 
    regex = r"\[[^\]]*\]\([^\)]*.md\)"
    new_text = md_text
    for match in re.finditer(regex, md_text):
        old_link = (match.group(0))
        new_link = (match.group(0).replace(".md]", ".html]").replace(".md)", ".html)"))
        new_text = new_text.replace(old_link, new_link)
    return new_text

# 保护美元符号
def wrap_raw_dollar(md_text):
    new_text = md_text
    new_text = new_text.replace(r"\$", RAW_DOLLAR)
    return new_text

# 渲染删除线
def render_del(md_text):
    regex = "~~[^~]*~~"
    new_text = md_text
    for match in re.finditer(regex, md_text):
        old_link = (match.group(0))
        new_link = ("<del>" + match.group(0)[2:-2] + "</del>")
        new_text = new_text.replace(old_link, new_link)
    return new_text

# 还原受保护的美元符号
def unwrap_raw_dollar(html_content):
    new_text = html_content
    new_text = new_text.replace(RAW_DOLLAR, "$")
    return new_text

# 从保护数据中反解出数学块内容
def unwrap_math_content(html_content):
    regex = MATH_CONTENT_BEGIN + r"[a-z0-9A-Z\=\+\-\/]+" + MATH_CONTENT_END
    new_text = html_content
    for match in re.finditer(regex, html_content):
        old_link = (match.group(0))
        new_link = old_link.replace(MATH_CONTENT_BEGIN, "").replace(MATH_CONTENT_END, "").strip()
        new_link = base64.b64decode(new_link).decode("utf-8")
        new_link = new_link.replace("<", r"\lt ").replace(">", r"\gt ")
        if new_link.startswith("$$"):
            new_text = new_text.replace(old_link, new_link)
        else:
            # 假设以一个 $ 开头
            new_text = new_text.replace(old_link, "\\(" +new_link[1:-1] + "\\)")
    return new_text

def unwrap_html_link(html_content):
    regex = HTML_LINK_BEGIN + r"[a-z0-9A-Z\=\+\-\/]+" + HTML_LINK_END
    new_text = html_content
    for match in re.finditer(regex, html_content):
        old_link = (match.group(0))
        new_link = old_link.replace(HTML_LINK_BEGIN, "").replace(HTML_LINK_END, "").strip()
        new_link = base64.b64decode(new_link).decode("utf-8")
        new_link = '<a href="%s">%s</a>' % (new_link, new_link)
        new_text = new_text.replace(old_link, new_link)
    return new_text

def get_menu_from_list(menu_list):
    content = '<section id="0"><a href="/README.html">返回首页</a></section>\n'
    content += '<h1>目录</h1>\n'
    for index, grade, value in menu_list:
        content += '<p style="margin-left: %dpx;"><a href="#%d">%s</a></p>\n' % (grade * 10, index, value)
    return content + "<hr>"

def html_make_title_menu_section(html_content): # 构建用于索引的目录
    regex = r"<h\d>(.|\n)+?</h\d>"
    new_text = html_content
    cnt = 0
    menu_list = []
    for match in re.finditer(regex, html_content):
        cnt += 1
        old_link = match.group(0)
        new_link = '<section id="%d"><a href="#%d">%s</a><a href="#0">(返回顶部)</a></section>\n' % (cnt, cnt, old_link)
        new_text = new_text.replace(old_link, new_link)
        menu_list.append((cnt, int(old_link[2]), old_link[4:-5]))
    menu_content = get_menu_from_list(menu_list)
    return new_text.replace("<body>", "<body>" + menu_content)

def save_file(new_file: str, html_content: str): # 减少硬盘写入次数
    try:
        old_content = open(new_file, "r", encoding="utf-8").read()
    except:
        old_content = None
    if old_content is None or old_content.strip() != html_content.strip():
        pub_mylog.log("- <<1;34[INFO]>>: \033[1;33mcreating\033[0m html file <<1;32[%s]>> ...\n" % new_file)
        open(new_file, "w", encoding="utf-8").write(html_content)
    else:
        pub_mylog.log("- <<1;34[INFO]>>: html file <<1;32[%s]>> \033[1;35munchanged\033[0m ...\n" % new_file)

# 为所有 markdown 文件制作 html 副本
def create_all_html_file():
    for old_file in pub_dir_utils.get_all_markdown_file():
        assert old_file.endswith(".md")
        markdown_content = pre_scan(open(old_file, encoding="utf-8").read())
        markdown_content = wrap_http_link(markdown_content) # 渲染管线
        markdown_content = render_del(markdown_content)
        markdown_content = rename_link(markdown_content)
        markdown_content = wrap_raw_dollar(markdown_content)
        markdown_content = wrap_math_content(markdown_content)
        html_content     = get_html_from_md(markdown_content) # 渲染 html
        html_content     = unwrap_math_content(html_content) # 渲染 html
        html_content     = unwrap_raw_dollar(html_content)
        html_content     = unwrap_html_link(html_content)
        html_content     = html_make_title_menu_section(html_content)
        new_file = old_file[:-3] + ".html"
        save_file(new_file, html_content)

def create_index_html():
    new_index_html = pub_dir_utils.get_root_dir("index.html")
    open(new_index_html, "w").write("""
<!DOCTYPE html>
<html>
    <head></head>
    <body></body>
    <script>window.location.href="/README.html";</script>
</html>
""")

if __name__ == "__main__":
    create_all_html_file()
    create_index_html()