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

# 中介常量：必须是随机的字母数字序列
RAW_DOLLAR         = generate_random_sequence(64)
MATH_CONTENT_BEGIN = generate_random_sequence(64)
MATH_CONTENT_END   = generate_random_sequence(64)

CDN = """
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
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
    {CDN}
</head>
<body>
    {html}
</body>
</html>
    """
    return html_with_mathjax

# 封装 http 和 https 链接
def wrap_http_link(md_text):
    regex = r"http(s)*://[^\s\n]+"
    new_text = md_text
    for match in re.finditer(regex, md_text):
        old_link = match.group(0)
        new_link = "[%s](%s)" % (old_link, old_link)
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

# 为所有 markdown 文件制作 html 副本
def create_all_html_file():
    for old_file in pub_dir_utils.get_all_markdown_file():
        pub_mylog.log("- <<1;34[INFO]>>: creating html file for <<1;32[%s]>> ...\n" % old_file)
        assert old_file.endswith(".md")
        markdown_content = open(old_file, encoding="utf-8").read()
        markdown_content = wrap_http_link(markdown_content) # 渲染管线
        markdown_content = render_del(markdown_content)
        markdown_content = rename_link(markdown_content)
        markdown_content = wrap_raw_dollar(markdown_content)
        markdown_content = wrap_math_content(markdown_content)
        html_content     = get_html_from_md(markdown_content) # 渲染 html
        html_content     = unwrap_math_content(html_content) # 渲染 html
        markdown_content = unwrap_raw_dollar(html_content)
        new_file = old_file[:-3] + ".html"
        open(new_file, "w", encoding="utf-8").write(html_content)

if __name__ == "__main__":
    create_all_html_file()