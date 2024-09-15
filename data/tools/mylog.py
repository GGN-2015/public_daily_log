import sys
import re

def replace_color(msg: str) -> str: # 注入颜色信息
    regex   = r"<<([^\[]*)\[([^\]]*)\]>>"
    new_msg = msg
    for match_pos in re.finditer(regex, msg):
        color_id = match_pos.group(1)
        content  = match_pos.group(2)
        raw_text = match_pos.group(0)
        new_msg  = new_msg.replace(raw_text, "\033[%sm%s\033[0m" % (color_id, content))
    return new_msg

def log(msg: str):
    msg = replace_color(msg)
    sys.stderr.write("%s\n" % msg.rstrip())