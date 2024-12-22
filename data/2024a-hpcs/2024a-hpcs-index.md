# 《高性能计算机体系结构和设计》课程笔记  

## 课程笔记

1. [2024-09-10_2024a-hpcs.md](../../data/2024a-hpcs/2024-09-10_2024a-hpcs.md)
2. [2024-09-24_2024a-hpcs.md](../../data/2024a-hpcs/2024-09-24_2024a-hpcs.md)
3. [2024-10-19_2024a-hpcs.md](../../data/2024a-hpcs/2024-10-19_2024a-hpcs.md)

## 课程信息

1. 课程微信群：【2024高性能计算机体系结构和设计】
2. `2024-11-21` 就高性能大作业汇报做了一个简单的分工：https://github.com/GGN-2015/hpc-course-presentation
3. `2024-11-30` 一定要在星期六一天之内把整个汇报整合工作全部完成。
4. `2024-12-03` 完成汇报，完结撒花。

## 课件列表

- 老师说课程 ppt 会发到 spoc 上，但是我去 spoc 上也没看到啊。。。。

> @所有人
> 同学们好，明天上课我们开始第一轮大作业汇报，请1-5组同学做好准备，组长上课前将报告和汇报PPT上传至以下北航云盘链接，并且上课时携带**两份打印的报告**到教室，谢谢！
> https://bhpan.buaa.edu.cn/link/AAABF0641341724062AAC41D74925F7735

- `2024-12-22` 打算补充一些 NUMA 相关的内容，主要参考博客：https://hackmd.io/@hPMCWajOS-ORQdEEAQ04-w/Hkd1rsonP
- 分类树：
  - UMA：内存均一：所有存储器在所有处理器视角下访问效率相同
  - NUMA：内存不均一：处理器能够更高效地访问离自己更近的存储器，访问其他处理器下的存储器需要借助通信
    - CC-NUMA：缓存一致的非均一内存访问：通过硬件上的缓存/内存一致性协议保证
    - NCC-NUMA：缓存不一致的非均一内存访问：硬件不保证一致性，通过软件约束避免并发故障
    - NORMA：硬件层面不直接提供的联机内存访问，多机之间的数据交换需要借助网络通信协议，常用于 MPP 和 Cluster。

- 一些关于 CXL 的话题
  - （2024）Computer Survey：An Introduction to the Compute Express Link (CXL) Interconnect
  - （2022）ASPLOS：Clio: a hardware-software co-designed disaggregated memory system
  - （2023）ASPLOS：Pond: CXL-Based Memory Pooling Systems for Cloud Platforms
  - （2023）ASPLOS：TPP: Transparent Page Placement for CXL-Enabled Tiered-Memory

