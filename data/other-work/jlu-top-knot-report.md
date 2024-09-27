 # 《扭结不变量区分能力报告》`2024-09-27`



## 不变量区分能力实验报告设计思路

- 先构建小于等于 11 crossing 的通用扭结数据库（这次我打算直接搞个 json 之类的）
  - 主键：扭结名称
  - 信息：khovanov 同调、HOMFLY-PT 多项式、补空间 Volume
- 然后再按照一定的判别标准划分等价类
  - 需要按照以下六种依据划分等价类
  - 仅 khovanov
  - 仅 HOMFLY-PT
  - 仅 Volume （`eps = 1e-4`）
  - **khovanov + HOMFLT-PT**
    - 目前大规模采用的等价类划分方案
    - 采用这种方案主要是出于部署便捷考虑
  - khovanov + Volume
  - HOMFLT-PT + Volume
  - khovanov + HOMFLT-PT + Volume
- 对于每种等价类划分标准
  - 出具一个原始统计信息文件，描述所有的等价类
  - 给出一个描述性的统计报告，不用字数很多，只需要考虑以下几点
    - k 元等价类的数目（k=1, 2, ...）
    - 手性的区分能力
- 需要指出的一些额外问题
  - 超时机制
    - HOMFLY-PT 和 Volume 在计算的过程中常常会出现程序难以终止的情况
    - 在这种情况下我们要求程序若 20 min 不能给出计算结果就强制终止它
    - 超时机制在一定程度上会减弱算法对扭结的识别能力

## 完成进度

- 感谢过去的自己给现在的自己留了一个好东西
  - 这里可以查到很多上文中需要的列表：https://github.com/TopologicalKnotIndexer
  - https://github.com/TopologicalKnotIndexer/HOMFLY-PT-polynomial-list/blob/main/data/HOMFLY-PT.txt
  - https://github.com/TopologicalKnotIndexer/khovanov-homology-list/blob/main/data/khovanov.txt
  - https://github.com/TopologicalKnotIndexer/volume_list/blob/main/src/volume_info_list.txt

- 首先检查一下这几个文件的行数是否是一样的
  - 是的，行数都是 1871 行
  - 但是这也说明了另一个问题：扭结的名称不是 “**规范名字**”
- 什么是规范名字
  - 对于非手性扭结，他的名字里不应该出现 `m` 前缀，但是文件中出现了如 `mK4a1` 的表示
  - 这意味着我们需要对名字进行规范化之后再使用这些文件
  - 名字规范化的项目：https://github.com/TopologicalKnotIndexer/knotname-reg
    - 这个项目没有依赖其他 repo, 可以放心 clone
- 如何对上面的三个列表进行规范化
  - 读取每一行内容，分离扭结名称和不变量
  - 对每行扭结名称进行规范化，生成一个新的文件
  - 根据扭结名称进行去重，保证每个扭结只有一条记录
  - 检查去重之后三个文件中的行数是否仍然一致，如果仍然一致，则基本上可以认为算法没有问题

- 写差不多了
  - 详见 https://github.com/TopologicalKnotIndexer/conflict_lab

