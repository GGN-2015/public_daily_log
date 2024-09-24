import subprocess
import functools
import datetime

def run_command(cmd: list):
    fp = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = fp.communicate("")
    stdout = stdout.decode("utf-8")
    stderr = stderr.decode("utf-8")
    returncode = fp.wait()
    return (returncode, stdout, stderr)

@functools.cache
def get_commit_list():
    ret, out, err = run_command(["git", "log", "--pretty=format:%H %s"])
    arr = []
    for term in out.split("\n"):
        term = term.strip()
        if term == "": continue # 跳过空行
        hash_code, commit_msg = (term.split(maxsplit=1))
        arr.append((hash_code, commit_msg))
    return arr

@functools.cache
def get_date_tag_list() -> list:
    arr = []
    for _, tag in get_commit_list():
        if tag.startswith("v") and tag not in arr:
            arr.append(tag)
    return sorted(arr)[::-1]

def get_last_commit_of_a_day(date_string) -> str: # 未找到返回初始 commit
    for line in get_commit_list():
        hash_code, msg_now = line
        if msg_now == date_string:
            return hash_code
    return get_last_commit_of_a_day("Initial commit")

def compare_commits(commit_hash_from, commit_hash_to): # 对比不同 commit 之间的差异
    ret, out, err = run_command(["git", "diff", "--shortstat", commit_hash_from, commit_hash_to])
    return out.strip()

def get_previous_day(date_str): # 获取前一天的日期
    date_format = "%Y-%m-%d" 
    given_date = datetime.datetime.strptime(date_str, date_format)
    previous_day = given_date - datetime.timedelta(days=1)
    return previous_day.strftime(date_format)

def get_last_date_tag(date_tag):
    return "v" + get_previous_day(date_tag[1:])

def gen_line_stat_content() -> str: # 生成行数统计信息
    content  = "# 《`GGN_2015` 的公开日志中每日新增行数情况》\n\n"
    content += "| 日期 | 修改信息 |\n"
    content += "| ---- | ----: |\n"
    for date_tag in get_date_tag_list():
        last_date_tag = get_last_date_tag(date_tag)
        previous_hash = get_last_commit_of_a_day(last_date_tag)
        now_hash      = get_last_commit_of_a_day(date_tag)
        change_info   = (compare_commits(previous_hash, now_hash))
        content += "| **%s** | %s |\n" % (date_tag[1:], change_info)
    return content

if __name__ == "__main__":
    print(gen_line_stat_content())