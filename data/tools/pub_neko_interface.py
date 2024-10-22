# 在共有仓库调用私有仓库中的 neko 命令
# 建议只做 bash 脚本调用，不要调用具体实现细节
import subprocess

def neko(*args) -> int:
    result = subprocess.run(['neko'] + list(args))
    return result.returncode