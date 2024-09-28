import pub_copy_std
import pub_gen_line_stat
import pub_gen_title_list
import pub_html_tool

def auto_pipeline(): # 自动化构建过程
    pub_copy_std.copy_std()
    pub_gen_line_stat.gen_line_stat_file()
    pub_gen_title_list.create_title_list_file()
    pub_html_tool.create_all_html_file()

if __name__ == "__main__":
    auto_pipeline()