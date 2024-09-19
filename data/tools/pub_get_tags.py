# 获取文章中的 json 对象

import json
import functools
import sys
import re

import pub_dir_utils

def get_json_object_in_markdown(file_content) -> dict:
    regex = r"\n```json[^`]*```\n"
    arr = {
        "tags": [] # 默认文件没有标签
    }
    for match in re.finditer(regex, file_content):
        json_object_str = match.group(0).strip()[7:-3].strip()
        json_object_raw = json.loads(json_object_str)
        if json_object_raw.get("tags") is not None: # 覆盖
            arr = json_object_raw
    return arr

@functools.cache
def get_json_object_in_file(filepath):
    return get_json_object_in_markdown(open(filepath).read())

# 列举所有具有某种标签的文件名
def show_all_file_with_tag(tag): 
    file_list = []
    for file in pub_dir_utils.get_all_markdown_file():
        json_desc = get_json_object_in_file(file)
        if tag == "--no-tag": # 筛选没有标签的文件
            if json_desc["tags"] == []:
                file_list.append(file)
        elif tag == "--all": # 显示所有可能的文件
            file_list.append(file)
        else:
            if tag in json_desc["tags"]:
                file_list.append(file)
    return file_list

if __name__ == "__main__":
    try:
        tag_name = sys.argv[1]
    except:
        tag_name = "--all" # 默认显示所有文件的标签
    arr = []
    for file in show_all_file_with_tag(tag_name):
        arr.append("%s: %s" % (get_json_object_in_file(file)["tags"], file))
    arr = sorted(arr)
    for line in arr:
        print(line)