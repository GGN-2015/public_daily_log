import markdown
import re
import pub_dir_utils
import pub_mylog

# 用于生成指定 markdown 文件的 html 版本
def get_html_from_md(md_text):
    html = markdown.markdown(md_text, extensions=['fenced_code', 'tables'])
    html_with_mathjax = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    {html}
</body>
</html>
    """
    return html_with_mathjax

# 将指向 markdown 文件的链接改为指向 html 文件的
def rename_link(md_text): 
    regex = r"\[[^\]]*\]\([^\)]*.md\)"
    new_text = md_text
    for match in re.finditer(regex, md_text):
        old_link = (match.group(0))
        new_link = (match.group(0).replace(".md]", ".html]").replace(".md)", ".html)"))
        new_text = new_text.replace(old_link, new_link)
    return new_text

# 为所有 markdown 文件制作 html 副本
def create_all_html_file():
    for old_file in pub_dir_utils.get_all_markdown_file():
        pub_mylog.log("- <<1;34[INFO]>>: creating html file for <<1;32[%s]>> ...\n" % old_file)
        assert old_file.endswith(".md")
        markdown_content = open(old_file, encoding="utf-8").read()
        markdown_content = rename_link(markdown_content)
        html_content     = get_html_from_md(markdown_content)
        new_file = old_file[:-3] + ".html"
        open(new_file, "w", encoding="utf-8").write(html_content)

if __name__ == "__main__":
    create_all_html_file()