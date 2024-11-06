# 为所有 markdown 文件生成 gemini 词向量嵌入
import google.generativeai as gemini
import json
import os
from tqdm import tqdm
import numpy as np
import pub_dir_utils

EMB_FILE_SUFFIX   = ".gemini004emb" # 不要修改这个
USE_MODEL         = 'models/embedding-001'
LENGTH_CONTENT    = 768
FORCE_REGEN       = False
MAX_TEXT_CHAR_CNT = 3000

def get_dot_product(vector_a, vector_b): # 计算余弦相似度
    vector_a    = np.array(vector_a)
    vector_b    = np.array(vector_b)
    dot_product = np.dot(vector_a, vector_b)
    return dot_product

def get_embedding_for_string(text: str, task_type): # 获得相似度词向量
    text = text[:MAX_TEXT_CHAR_CNT]
    guess_title = (
        text.split("\n")[0].strip() 
        if task_type.upper()=="RETRIEVAL_DOCUMENT" 
        else None
    )
    response = gemini.embed_content(
        model=USE_MODEL,
        content=text,
        task_type=task_type,
        title=guess_title
    )
    return response['embedding']

def get_last_modified_timestamp(file_path): # 获取文件的上次修改时间, 如果文件不存在，返回 0
    try:
        last_modified_time = os.path.getmtime(file_path)
    except FileNotFoundError:
        last_modified_time = 0
    return last_modified_time

def get_file_content_safe(emb_file_name) -> str: # 安全地读取文件内容
    if not os.path.isfile(emb_file_name):
        return ""
    return open(emb_file_name, "r", encoding="utf-8").read()

def get_embedding_for_file(filenow) -> str: # 读取文件内容, 计算词向量
    file_content = get_file_content_safe(filenow)
    return get_embedding_for_string(file_content, "RETRIEVAL_DOCUMENT")

def write_into_file(content: str, file: str): # 将内容写入文件
    fp = open(file, "w", encoding="utf-8")
    fp.write(content)
    fp.close()

def save_embedding_content(emb_file_name, emb_content):
    emb_str_content = json.dumps(emb_content)
    if emb_str_content != get_file_content_safe(emb_file_name): # 如果两个字符串不同，就保存一下
        write_into_file(emb_str_content, emb_file_name)

def get_emb_file_for_markdown(markdown_file: str): # 获得指定的词向量文件
    assert markdown_file.endswith(".md")
    return markdown_file[:-3] + EMB_FILE_SUFFIX

def create_work_embedding_for(filenow: str): # 为指定的文件生成词向量嵌入文件
    emb_file_name = get_emb_file_for_markdown(filenow)
    if FORCE_REGEN or get_last_modified_timestamp(emb_file_name) < get_last_modified_timestamp(filenow):
        emb_content = get_embedding_for_file(filenow)
        save_embedding_content(emb_file_name, emb_content)

def get_min_cos_distance(arr2d_or_1d, guide_embedding):
    if len(np.array(arr2d_or_1d).shape) == 1: # 保证是一个二维向量
        arr2d_or_1d = [arr2d_or_1d]
    return max([
        get_dot_product(arr1d, guide_embedding)
        for arr1d in arr2d_or_1d
    ])

def get_cos_distance_for_file_and_vector(filenow: str, guide_embedding) -> float: # 计算文章和指定词向量的余弦相关性
    emb_file = get_emb_file_for_markdown(filenow)
    fp = open(emb_file, "r")
    arr2d_or_1d = json.load(fp)
    fp.close()
    return get_min_cos_distance(arr2d_or_1d, guide_embedding)

def get_relevant_rank(guide_text) -> list: # 按照与某个指定词语的相关性对内容进行排序：
    get_all_embedding_value()              # 先处理好所有词嵌入的值
    guide_embedding = get_embedding_for_string(guide_text, "RETRIEVAL_QUERY")
    if len(guide_embedding) != LENGTH_CONTENT: # 如果导引检索内容被分段了，只选择其中的第一段内容作为参考依据
        guide_embedding = guide_embedding[0]
        assert len(guide_embedding) == LENGTH_CONTENT
    arr = []
    all_markdown_file = pub_dir_utils.get_all_markdown_file()
    for i in tqdm(range(len(all_markdown_file))): # 枚举所有文件并生成指定的词嵌入文件
        filenow = all_markdown_file[i]
        arr.append((filenow, get_cos_distance_for_file_and_vector(filenow, guide_embedding)))
    return sorted(arr, key=lambda x:x[1], reverse=True)

def get_all_embedding_value():
    all_markdown_file = pub_dir_utils.get_all_markdown_file()
    for i in tqdm(range(len(all_markdown_file))): # 枚举所有文件并生成指定的词嵌入文件
        filenow = all_markdown_file[i]
        create_work_embedding_for(filenow)

if __name__ == "__main__":
    api_key = input("api_key>>>") # configure api_key
    gemini.configure(api_key=api_key)
    for file in get_relevant_rank("Scientific computing visualization"):
        print(file[1], file[0])
