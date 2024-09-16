# 检查公开日志中文件名的合法性
# 写得太丑陋了，以后回来改

import os
import dir_utils
import re
from mylog import log
from dup_name_check import dup_name_dict

def check_lower_alpha_digit(s: str): # 检查是否只有小写字母和数字
    for c in s:
        if c.isalpha():     # 如果是字母
            if c.isupper(): # 出现了大写字母
                return False
        elif c.isdigit():
            continue
        else:
            return False # 出现了字母和数字之外的符号
    return True

def check_lower_alpha_digit_dash(s: str): # 检查小写字母数字连字符
    for c in s:
        if c.isalpha():     # 如果是字母
            if c.isupper(): # 出现了大写字母
                return False
        elif c.isdigit():
            continue
        elif c == "-": # 出现了连字符
            continue
        else:
            return False # 出现了字母和数字之外的符号
    return True

def check_lower_alpha_digit_underline(s: str): # 检查小写字母数字下划线
    for c in s:
        if c.isalpha():     # 如果是字母
            if c.isupper(): # 出现了大写字母
                return False
        elif c.isdigit():
            continue
        elif c == "_": # 出现了连字符
            continue
        else:
            return False # 出现了字母和数字之外的符号
    return True

def date_format_check(s: str) -> bool:
    return bool(
        re.match(r"^\d\d\d\d$", s) or        # 年
        re.match(r"^\d\d\d\d-\d\d$", s) or   # 月
        re.match(r"^\d\d\d\d-\d\d-\d\d$", s) # 日
    )

def avai_name_check(filename) -> bool: # 检查文件名是否合法
    if filename.find(".") == -1: # 文件名必须有拓展名
        return False
    if len(filename.split(".")) != 2: # 文件有且只有一个拓展名
        return False
    lpart, rpart = filename.split(".")
    if not check_lower_alpha_digit(rpart): # 检查文件拓展名中只能有小写字母和数字
        return False
    if rpart == "py": # 对于 python 程序，我们额外豁免了一类文件名
        flag = check_lower_alpha_digit_underline(lpart)
        if flag:
            return True
    if lpart.find("_") == -1: # 没有连字符
        return check_lower_alpha_digit_dash(lpart)
    else:
        if len(lpart.split("_")) != 2: # 文件有且只有一个下划线
            return False
        l1, l2 = lpart.split("_") # l1 必须是类似日期的形式，l2 中只能由字母数字和连字符
        return (
            date_format_check(l1) and
            check_lower_alpha_digit_dash(l2)
        )

def get_filename_list() -> list: # 获取文件名列表
    arr = []
    for name in dup_name_dict():
        arr.append(name)
    return sorted(arr)

def main():
    cnt = 0
    for name in get_filename_list():
        if not avai_name_check(name):
            log("- <<1;34[INFO]>>: bad name found: <<1;33[%s]>>" % name)
            cnt += 1
    if cnt == 0:
        log("- <<1;32[SUCCESS]>>: no bad name found.")
    else:
        log("- <<1;31[ERROR]>>: <<1;33[%d]>> bad name(s) found." % cnt)

if __name__ == "__main__":
    main()
