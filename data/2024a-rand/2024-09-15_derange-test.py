# 基于随机试验的错排概率分析
import random
import math
from tqdm import tqdm

def derange_check(arr: list): # 检查是否是错排
    for idx, val in enumerate(arr):
        if idx == val: # 只要出现了位置等于编号的情况，就说明不是错排
            return False
    return True

def gen_random_arr(n: int) -> list: # 生成随机排列
    arr = [i for i in range(n)]
    random.shuffle(arr)
    return arr

def get_p(n: int, test_cnt=1000000) -> float: # 计算错排概率
    is_derange_cnt = 0
    for _ in tqdm(range(test_cnt)):
        arr = gen_random_arr(n)
        if derange_check(arr):
            is_derange_cnt += 1
    return is_derange_cnt / test_cnt

def main():
    print("derange probability: %.12f" % get_p(100))
    print("                1/e: %.12f" % (1 / math.e))

if __name__ == "__main__":
    main()
