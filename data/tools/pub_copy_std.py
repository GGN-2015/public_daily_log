import pub_dir_utils
import pub_mylog

def copy_std(): # 从日常生活规范项目拷贝一个 README.md 过来
    filefrom = pub_dir_utils.get_std_readme_dir()
    fileto   = pub_dir_utils.get_root_dir("data", "auto-gen", "life-standard.md")
    content  = open(filefrom, "r", encoding="utf-8").read()
    pub_mylog.log("- <<1;34[INFO]>>: copying std markdown ...")
    open(fileto, "w", encoding="utf-8").write(content)

if __name__ == "__main__":
    copy_std()