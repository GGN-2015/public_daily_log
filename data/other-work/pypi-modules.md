# 《`GGN_2015` 打包的一些 pypi 包》

- 总览 https://pypi.org/user/GGN_2015/
- `GGN_2015` 在制作 pypi 包时应尽可能使用英文编写 README 文档

## 注意事项

- 使用 `twine` 前要提前配置 `cat ~/.pypirc`
  - 先去 https://pypi.org/manage/account/ 生产 `API token`
  - 然后修改 `~/.pypirc` 的内容为

```toml
[pypi]
  username = __token__
  password = <"pypi-" 开头的 API token>
```

## 构建过程

- 选个好名字，到 https://pypi.org/search/ 上进行查询，看看是有重名包
  - 一般来说，如果有名字冲突，在 `twine` 上传时会遇到报错
- 在指定名子的子目录中编写代码 `__init__.py` 和测试
- 编写 `MANIFEST.IN` 以及 `pyproject.toml`
  - `pyproject.toml` 指明版本号，保证同一版本号在上传时仅仅使用一次，使用语义化版本控制
  - `MANIFEST.IN` 指明哪些文件应该在打包时被忽略
- 执行 `python -m build` 进行构建
- 执行 `twine upload dist/*` 进行上传

## `GGN_2015` 目前制作的一些包

- `2024-10-12` 远程命令发送：https://pypi.org/project/neko-rexec/
- `2024-10-12` 发文件拆分为片段：https://pypi.org/project/cuffers/
- `2024-10-12` 简单多线程加速：https://pypi.org/project/mptrolley/
- `2024-10-21` 在 CT 图像中识别标志球：https://pypi.org/project/dcm-ball-detector/
- `2024-10-25` 多进程并行基础设施：https://pypi.org/project/process-wrap-queue/
  - 使用 process-wrap-queue 重新实现了 mptrolley
  - 目前总是会遇到打开文件过多的报错，以后想办法看看能不能解决一下

