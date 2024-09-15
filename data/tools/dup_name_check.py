# 检查公开日志中是否有重复出现的文件名

import os
import dir_utils
from mylog import log

def dup_name_dict() -> dict: # 获得重名检查 dict
    dic = {}
    for file in dir_utils.get_all_file_in_this_project():
        basename = os.path.basename(file)
        if dic.get(basename) is None: # 初始化列表
            dic[basename] = []
        dic[basename].append(file)
    return dic

def dup_name_check(): # 输出所有重名文件的重名情况
    dic = dup_name_dict()
    cnt = 0
    for term in dic:
        if len(dic[term]) >= 2:
            log("- <<1;34[INFO]>>: duplicated name <<1;33[%s]>>" % term)
            for file in dic[term]:
                log("  - %s" % file)
            cnt += 1 # 记录找到了多少组重名文件
    if cnt == 0:
        log("- <<1;32[SUCCESS]>>: no duplicated filename found.")
    else:
        log("- <<1;31[ERROR]>>: <<1;33[%d]>> duplicated filename(s) found." % cnt)

if __name__ == "__main__":
    dup_name_check()