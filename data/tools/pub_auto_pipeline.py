import pub_copy_std
import pub_gen_line_stat
import pub_gen_title_list
import pub_html_tool
import pub_neko_interface

def render_public():
    pub_copy_std.copy_std()
    pub_gen_line_stat.gen_line_stat_file()
    pub_gen_title_list.create_title_list_file()
    pub_html_tool.create_all_html_file()

def auto_pipeline(): # 自动化构建过程
    render_public()
    pub_neko_interface.neko("send_blog") # 远程调用公有仓库中的代码
    pub_neko_interface.neko("push")

if __name__ == "__main__":
    auto_pipeline()