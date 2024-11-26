# 《`GGN_2015` 拓扑学相关工作的公开日志》

## 2024-11

- `2024-11-16` 参加东北拓扑系列活动。
- `2024-11-18` 实现了一个用于计算链环 n-cabling 的程序，但是现在还没有进行充分的测试。
  - 项目地址：https://github.com/GGN-2015/pd-code-n-cabling
- `2024-11-21` 将来需要完成的工作：
  - 短时间内交
    - 编写一个从图像中读取扭结信息，输出扭结或者链环 PD_CODE 的程序。
  - 较长期交付：
    - 编写一个能够将任意链环的三维空间坐标转换为 PD_CODE 的程序。
    - 编写使用素链环构建非素链环数据库的程序。
- `2024-11-26` 创建了 knotpen 项目。

## 2024-10

- `2024-10-02` 在统计报告中增加了《联合使用 khovanov 同调、HOMFLY-PT 多项式以及 volume 的区分能力》一节。
- `2024-10-04` 在报告中添加了冲突相关的具体数据。
- `2024-10-22` 这篇文章中提到了使用机器学习预测扭结类型的思路，可以触控看看
  - https://mp.weixin.qq.com/s/WmQ-GN1IVehXI7oLdGFuVw
- `2024-10-23` 尝试制作 `colored_jones_2` 和 `colored_jones_3` 的基础分类信息
  - 制作了复合扭结的 `pd_code` 列表：https://github.com/TopologicalKnotIndexer/com_pd_code_list/blob/main/data/com_pd_code_list.txt
- `2024-10-24` `colored_jones_2` 和 `colored_jones_3` 合计只有 `32.3%` 的数据能够进行计算。
- `2024-10-24` 编写了一个多进程并行的基础函数库，将来计划合并进入 `mptrolley`。
- `2024-10-25` 计算所有标准扭结 `pd_code` 的 `writhe`。
- `2024-10-27` 在 `sagemath` 的论坛上发了一个帖子，讨论关于 `colored_jones_polynomial` 不返回的问题。
  - https://ask.sagemath.org/question/79833/colored-jones-polynomial-function-does-not-return/
  - 记得每天去看一眼这个帖子是否有人回复。
- `2024-10-28` 关于 sagemath colored jones 的帖子：
  1. Max Alekseyev: Please submit a bugreport to https://github.com/sagemath/sage/issues
  2. 我打算搞个 ubuntu 的虚拟机去做个复现，毕竟 AOSC 有点太小众了还是。
  3. 写了一个 issue（bugreport）：https://github.com/sagemath/sage/issues/38869

## 2024-09

- `2024-09-27` 在私有日志中仍保留了大量相关工作的具体细节信息。
- `2024-09-29` 计划出具小于等于 11 crossing 前提下的扭结不变量区分能力报告。
  - 详见：[jlu-top-knot-report.md](../../data/other-work/jlu-top-knot-report.md)

