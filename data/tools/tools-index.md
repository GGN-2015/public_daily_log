# 《`GGN_2015` 的公开日志工具清单》 

- 注：此文件可以被 `neko help` 命令读取进而提供功能的帮助，需要尊重私有日志中给出的规范填写。
- `pub_auto_pipeline.py`：HTML 渲染流水线，用于自动化执行行数统计脚本、拷贝日常生活规范、生成标题索引文件、构建 HTML 文件合集。
- `pub_avai_name_check.py`：检查公开日志项目中是否有不符合规定要求的文件名。
- `pub_copy_std.py`：从隔壁项目拷贝日常生活规范。
- `pub_dir_utils.py`：扫描项目中的所有文件。
- `pub_dup_name_check.py`：检查公开日志项目中是否有文件重名。
- `pub_gen_line_stat.py`：根据 gitlog 获取行数统计信息文件。
- `pub_gen_title_list.py`：生成标题索引文件。
- `pub_get_tags.py`：【管道工具】，在公开日志中使用 tags json 标签检索文件。
- `pub_git_utils.py`：根据 gitlog 获取行数统计信息字符串。
- `pub_html_tool.py`：渲染所有 markdown 文件到 HTML 文件。
- 公式测试：$f(x)=\frac{1}{\sqrt{2\pi}\sigma}\cdot\exp\left(-\frac{1}{2}\frac{(x-a)^2}{\sigma^2}\right)$

