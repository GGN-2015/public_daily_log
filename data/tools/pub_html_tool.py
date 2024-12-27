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
RAW_DOLLAR                     = generate_random_sequence(64)
MATH_CONTENT_BEGIN             = generate_random_sequence(64)
MATH_CONTENT_END               = generate_random_sequence(64)
HTML_LINK_BEGIN                = generate_random_sequence(64)
HTML_LINK_END                  = generate_random_sequence(64)
OFFCANVAS_CONTENT_PALCE_HOLDER = generate_random_sequence(64)

CDN = """
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
"""

NAVBAR = """
<nav class="navbar navbar-expand-lg bg-body-tertiary sticky-top" style="background-color: rgb(34, 139, 34) !important;">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">GGN_2015 的公开日志</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/README.html">返回首页</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasScrolling" aria-controls="offcanvasScrolling">目录</a>
        </li>
        <li class="nav-item">
            <a class="nav-link active" href="https://beian.miit.gov.cn/#/Integrated/recordQuery">辽ICP备2020011946号-1</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-warning" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
"""

OFFCANVAS = f"""
<div class="offcanvas offcanvas-start" data-bs-backdrop="true" tabindex="-1" id="offcanvasScrolling" aria-labelledby="offcanvasScrollingLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasScrollingLabel">目录</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    {OFFCANVAS_CONTENT_PALCE_HOLDER}
  </div>
</div>
"""

STYLE="""
<style>
    blockquote {
        border-left: 4px solid #007bff;
        padding-left: 1rem;
        border-radius: 0.25rem;
        font-style: italic;
    }
</style>
"""

# 用于生成指定 markdown 文件的 html 版本
def get_html_from_md(md_text: str):
    html = markdown2.markdown(md_text, extras=['mathjax', "fenced-code-blocks", "code-friendly", 'tables'])
    html, offcanvas_content = html_make_title_menu_section(html)
    html_with_mathjax = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    {STYLE}
</head>
<body data-bs-theme="dark">
    {NAVBAR}
    {OFFCANVAS}
    <div data-bs-spy="scroll" data-bs-target="#navbar-example2" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true" class="scrollspy-example bg-body-tertiary p-3 rounded-2" tabindex="0">
        {html}
    </div>
    {CDN}
    <script>
        function removeHashAndAfter(str) {{
            const hashIndex = str.indexOf('#');
            if (hashIndex !== -1) {{
                return str.slice(0, hashIndex);
            }}
            return str;
        }}
        function jump_to_lable(label_id) {{
            window.location.href = removeHashAndAfter(window.location.href) + "#scrollspyHeading" + label_id;
        }}
        const myOffcanvas = document.getElementById('offcanvasScrolling')
        myOffcanvas.addEventListener('hidden.bs.offcanvas', event => {{
            location.reload();
        }})
    </script>
</body>
</html>
    """.replace(OFFCANVAS_CONTENT_PALCE_HOLDER, offcanvas_content)
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

# 特殊处理 latex 中的 text 字段
def process_text_wrap(html_content):
    regex = r"\\text{.*?}"
    output_val = html_content
    for match in re.finditer(regex, html_content):
        old_content = match.group(0)
        new_content = old_content.replace(r"\;", " ").replace(r"\lt", r"} \lt \text{").replace(r"\gt", r"} \gt \text{")
        output_val = output_val.replace(old_content, new_content)
    return output_val

# 从保护数据中反解出数学块内容
def unwrap_math_content(html_content):
    regex = MATH_CONTENT_BEGIN + r"[a-z0-9A-Z\=\+\-\/]+" + MATH_CONTENT_END
    new_text = html_content
    for match in re.finditer(regex, html_content):
        old_link = (match.group(0))
        new_link = old_link.replace(MATH_CONTENT_BEGIN, "").replace(MATH_CONTENT_END, "").strip()
        new_link = base64.b64decode(new_link).decode("utf-8")
        new_link = process_text_wrap(new_link.replace("<", r" \lt ").replace(">", r" \gt "))
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
    content = ''
    for index, grade, value in menu_list:
        content += '<a style="margin-left: %dpx;" class="nav-link" onclick="jump_to_lable(%d)">%s</a>' % (grade * 10, index, value)
    return content

def html_make_title_menu_section(html_content: str): # 构建用于索引的目录
    regex = r"<h\d>(.|\n)+?</h\d>"
    new_html = html_content
    cnt = 0
    menu_list = []
    for match in re.finditer(regex, html_content):
        cnt += 1
        old_link      = match.group(0)
        title_content = old_link[4:-5]
        title_level   = int(old_link[2])
        title_index   = cnt
        new_link      = '<h%d id="scrollspyHeading%d">%s</h%d>' % (title_level, title_index, title_content, title_level)
        new_html = new_html.replace(old_link, new_link)
        menu_list.append((title_index, title_level, title_content))
    menu_content = get_menu_from_list(menu_list)
    return new_html, menu_content

def save_file(new_file: str, html_content: str): # 减少硬盘写入次数
    try:
        old_content = open(new_file, "r", encoding="utf-8").read()
    except:
        old_content = None
    if old_content is None or old_content.strip() != html_content.strip():
        pub_mylog.log("- <<1;34[INFO]>>: \033[1;33mcreating\033[0m html file <<1;32[%s]>> ...\n" % new_file)
        open(new_file, "w", encoding="utf-8").write(html_content)
    else:
        # pub_mylog.log("- <<1;34[INFO]>>: html file <<1;32[%s]>> \033[1;35munchanged\033[0m ...\n" % new_file)
        pass

def process_table_class(html_content: str) -> str:
    return html_content.replace("<table>", "<table class=\"table table-striped\">")

# 渲染单个 html 页面
def get_html_content_for_markdown(filename):
    markdown_content = pre_scan(open(filename, encoding="utf-8").read())
    markdown_content = wrap_http_link(markdown_content) # 渲染管线
    markdown_content = render_del(markdown_content)
    markdown_content = rename_link(markdown_content)
    markdown_content = wrap_raw_dollar(markdown_content)
    markdown_content = wrap_math_content(markdown_content)
    html_content     = get_html_from_md(markdown_content) # 渲染 html
    html_content     = unwrap_math_content(html_content) # 渲染 html
    html_content     = unwrap_raw_dollar(html_content)
    html_content     = unwrap_html_link(html_content)
    html_content     = process_table_class(html_content)
    return html_content

# 生成 index 目录
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

# 为所有 markdown 文件制作 html 副本
def create_all_html_file():
    for old_file in pub_dir_utils.get_all_markdown_file():
        assert old_file.endswith(".md")
        html_content = get_html_content_for_markdown(old_file)
        new_file     = old_file[:-3] + ".html"
        save_file(new_file, html_content)
    create_index_html()

if __name__ == "__main__":
    create_all_html_file()