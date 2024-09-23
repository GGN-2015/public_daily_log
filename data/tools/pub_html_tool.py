import markdown2
import re
import pub_dir_utils
import pub_mylog

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

# 对数学公式中的 "\" 字符数量进行翻倍
def pre_math_keep_slash_type1(md_text):
    regex    = r"\$[^\$\n]+\$"
    new_text = md_text
    for match in re.finditer(regex, md_text):
        old_link = (match.group(0))
        new_link = (match.group(0)).replace("\\", "\\\\")
        new_text = new_text.replace(old_link, new_link)
    return new_text

# 对数学公式中的 "\" 字符数量进行翻倍
def pre_math_keep_slash_type2(md_text):
    regex    = r"\$\$[^\$]+\$\$"
    new_text = md_text
    for match in re.finditer(regex, md_text):
        old_link = (match.group(0))
        new_link = (match.group(0)).replace("\\", "\\\\")
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

# 渲染删除线
def render_del(md_text):
    regex = "~~[^~]*~~"
    new_text = md_text
    for match in re.finditer(regex, md_text):
        old_link = (match.group(0))
        new_link = ("<del>" + match.group(0)[2:-2] + "</del>")
        new_text = new_text.replace(old_link, new_link)
    return new_text

# 渲染行内数学公式
def render_math_in_line(html_text):
    regex    = r"[^\$](\$[^\$\n]+\$)[^\$]"
    new_text = html_text
    for match in re.finditer(regex, html_text):
        old_link = (match.group(1))
        new_link = ("\\(" + match.group(1)[1:-1] + "\\)").replace("<em>", "_").replace("</em>", "_")
        new_text = new_text.replace(old_link, new_link)
    return new_text

# 删除数学公式中的 <em>
def del_em_in_math_content(html_text):
    regex    = r"\$\$[^\$]+\$\$"
    new_text = html_text
    for match in re.finditer(regex, html_text):
        old_link = (match.group(0))
        new_link = (match.group(0)).replace("<em>", "_").replace("</em>", "_")
        new_text = new_text.replace(old_link, new_link)
    return new_text

# 为所有 markdown 文件制作 html 副本
def create_all_html_file():
    for old_file in pub_dir_utils.get_all_markdown_file():
        pub_mylog.log("- <<1;34[INFO]>>: creating html file for <<1;32[%s]>> ...\n" % old_file)
        assert old_file.endswith(".md")
        markdown_content = open(old_file, encoding="utf-8").read()
        markdown_content = wrap_http_link(markdown_content) # 渲染管线
        markdown_content = pre_math_keep_slash_type1(markdown_content)
        markdown_content = pre_math_keep_slash_type2(markdown_content)
        markdown_content = rename_link(markdown_content)
        markdown_content = render_del(markdown_content)
        html_content     = get_html_from_md(markdown_content)
        html_content     = render_math_in_line(html_content)
        html_content     = del_em_in_math_content(html_content)
        new_file = old_file[:-3] + ".html"
        open(new_file, "w", encoding="utf-8").write(html_content)

if __name__ == "__main__":
    create_all_html_file()