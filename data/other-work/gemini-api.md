# 《学习 gemini api》

- `2024-11-06` 看到一个谈到词向量嵌入的文章，我觉得挺有同感的，其实我之前也想过这个问题。
  - https://technicalwriting.dev/data/embeddings.html
  - 于是打算学一波：https://pypi.org/project/google-generativeai/
- 看看这个：https://aistudio.google.com/prompts/new_chat
  - 生成了一个 API key（不宜公开）

- 创建了一个 conda 环境：google_env
- 如何获取一个段落的嵌入向量

```python
import google.generativeai as gemini

api_key = input("api_key>>>").strip()
gemini.configure(api_key=api_key)

text = 'Hello, world!'
response = gemini.embed_content(
    model='models/text-embedding-004',
    content=text,
    task_type='SEMANTIC_SIMILARITY'
)
embedding = response['embedding']
```

- 如何获取一个段落补全

```python
import google.generativeai as genai
import os

api_key = input("api_key>>>").strip()
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("The opposite of hot is")
print(response.text)
```

