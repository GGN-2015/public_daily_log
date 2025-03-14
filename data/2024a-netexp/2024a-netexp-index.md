# 《计算机网络与通信实验》课程笔记

## 置顶信息

- 网课链接：https://www.xuetangx.com/course/buaaP0812011754/21562422?channel=i.area.manual_search
- 课程教材：
  - http://premierbob.club:5001/computer-science/network-lab-buaa.pdf
  - 计算机网络实验教程（第三版）
- 实验报告：[2024-10-13_netlab-report.pdf](../../blob/pdf/2024-10-13_netlab-report.pdf)
- 课程通知：https://docs.qq.com/doc/DVVNkSWVvWXp4ZU1u
- 常见问题：https://docs.qq.com/doc/DVXJTdkV1UFJFcWZz
- 学堂在线：https://www.xuetangx.com/
  - 线上课程 DDL：`2025-01-14` 
- 文件传输：`ftp://10.111.1.29`
- 由于设备原因，我们从第 6 组机器移动到了第 5 组机器，我在第 4 组机器考试。

## 笔记信息

1. [2024-09-11_2024a-netexp.md](../../data/2024a-netexp/2024-09-11_2024a-netexp.md)
2. [2024-09-12_2024a-netexp.md](../../data/2024a-netexp/2024-09-12_2024a-netexp.md) 预习
3. [2024-09-25_think.md](../../data/2024a-netexp/2024-09-25_think.md) 一些思考
4. `2024-09-20` 写了一个长达 5 页的 OSPF 预习笔记，但是我好伤感，现在不想录入。（`2024-10-13` 决定放弃录入，直接归档纸质材料。）
   1. 以后还是要先把线下实验都跑通再搞别的。
   2. 周六下午和晚上可以重新去做实验。
5. [2024-10-17_2024a-netexp.md](../../data/2024a-netexp/2024-10-17_2024a-netexp.md) 预习

## 课程信息

1. 课程微信群名称：【2024秋计算机网络与通信实验】
2. 课程小班微信群：【周五下午-计网实验】
3. `2024-09-10` ZLJ 老师在微信群中发布消息：

> 同学们好，按照学校规定，中秋节和国庆节停课不上课。
> 下周二中秋节下午和晚上的课顺延至下下周二（9月24日）相同时段。
> 后续我们再跟相关同学商量找时间补课，拉齐进度。
> 初步打算**明天周三中午一点**(`2024-09-11`)用腾讯会议方式，介绍一下课程及课程安排。
> 因为选课人数超过100，正在OA申请学校大型腾讯会议，有结果会在群里通知。

3. `2024-09-11` ZLJ 老师录制了时长六十分钟左右的线上会议

> @所有人 录制：ZLJ 预定的会议
> 日期：2024-09-11 13:03:16
> 录制文件：https://meeting.tencent.com/v2/cloud-record/share?id=2dd1514e-1aa1-4665-9d0b-6255b6e40229&from=3&is-single=false&record_type=2
> 访问密码：【不宜公开，具体参考 `GGN_2015` 的日常生活日志 `2024-09-11` 之记录（非公开）】

4. 可以在高等教育出版社的网站上搜到免费的教材书
   1. 目前链接如下：https://ebook.hep.com.cn/index.html#/reader?bookId=1060860650378493952
   2. 书名《计算机网络实验教程（第二版）》作者：钱德沛、张力军
5. 慕课
   1. 在学堂在线网站：https://www.xuetangx.com/
   2. 搜索：计算机网络与通信实验
6. 校内共享资源（仅限校园网内使用）
   1. `ftp://10.111.1.29`；使用 `FileZilla` 连接即可
   2. 其中有部分资料是不宜公开的内部资料，在本项目中不得提及，在进行相关记录时需要非常注意这一点。
7. `2024-09-18` ZLJ 老师在微信群发言：

> 附件上IS-IS路由协议相关材料，套件2的同学请提前了解一下。课堂上通过几个简单实验，对比OSPF协议，对IS-IS协议一个初步了解。
>
> 常见问题解答文档见：https://docs.qq.com/doc/DVXJTdkV1UFJFcWZz

8. `2024-09-20` 参加了第一次线下实验课，但是做得很不好，总结了一下失误的地方。
   1. 一定要保证在线上实验完全调通再去做线下实验。
   2. 带能用的水性笔，不要到了之后没有笔用。
   3. 带修正带，实验材料里的格子很小，写错了没有地方涂改。
9. `2024-09-21` ZLJ 老师在微信群发言：

> 同学们好！
> 研究生网络实验第一周（9月16日--9月22日）实验内容及安排详见：
> 【腾讯文档】2024年秋季计算机网络与通信实验课程通知 https://docs.qq.com/doc/DVVNkSWVvWXp4ZU1u
>
> 另外，9月17日因中秋节放假停课，课程顺延至下周二对应时段。

10. `2024-09-25` 本周实验内容 **套件1（基础型）**:

> 1. 实验内容：OSPF协议实验
>    1. OSPF协议概述及基本配置
>    2. OSPF协议报文交互过程
>    3. OSPF协议链路状态描述
>    4. 区域划分与 LSA 种类
>    5. OSPF协议路由计算
>    6. OSPF协议组网设计（在线实验平台完成）
> 2. 实验前，观看相关内容的实验讲解视频，认真阅读相关实验内容原理和实验操作步骤说明。并在MOOC网站上完成OSPF协议实验的练习题部分并请实验前阅读“常见问题解答文档”的问题 51-62

11. `2024-09-27` 基本上勉强完成了任务，下次要注意磨刀不误砍柴工，重新配环境一定要 reset saved-configuration。
    1. 还有就是应该把网线带过去，上次忘带了。
12. `2024-09-28` ZLJ 发言：

> @所有人 这学期研究生“计算机网络与通信实验”课程开课实验班有10个：
> 周二下午、周二晚上、周三晚上、周四上午、周四晚上、周五上午、周五下午、周六下午、周六晚上、周日下午
>
> 同学们好！
> 研究生网络实验第三周（9月30日--10月6日）实验内容及安排详见：
> 【腾讯文档】2024年秋季计算机网络与通信实验课程通知 https://docs.qq.com/doc/DVVNkSWVvWXp4ZU1u

13. `2024-10-08` ZLJ 发言 (关于线上组网实验)：

> @所有人 关于**组网设计实验**的实验报告提交方式：
> 1.如果在线实验平台完成，设计型实验可以提交电子版word实验报告，以截屏方式保存核心配置和实验结果至Word文件。文件命名方式：实验班号-组号座位号-姓名学号，例如周一上午-10B-张三SY2106888
> 2.如果实验室线下完成或者eNSP模拟软件完成，请参照考试上传所有设备配置要求，将最终设备配置以及实验成功测试信息，保存到一个文本文件，命名方式同上。
> 最后，相关文件上传至ftp://10.111.1.29/upload/研究生对应文件夹下
>
> - `2024-10-10` **这个实验我还没做！**
> - `2024-10-17` 这个实验提交了。

14. `2024-10-17` 为了上传实验材料，下载了 `FileZilla`
    1. `sudo oma install filezilla`
    2. 字符编码问题：
       1. https://help.aliyun.com/zh/cloud-web-hosting/support/using-filezilla-garbled-words-for-connection-to-the-site
       2. https://blog.csdn.net/java_huashan/article/details/49421525
    3. 你别说，修好了字符集问题后，还真能用。
15. `2024-11-08` OSPF 一定要记得让所有相邻网段都用命令 `network` 挂一下，否则有些地方会看不见。
16. `2024-12-06` 计算机网络与通信实验：完结撒花！！！
    1. 感觉我还是有贡献的，告诉了老师 Shift+Backspace 和 Backspace 的事情，老师说头一次知道。
    2. 还有就是提了几个关于教材的建议：电子教材 & 突出问题方便定位等考虑。
17. SRv6 下的名词解释：
    1. SRv6 BE：Segment Routing over IPv6 Backbone
    2. SRv6 TE：Segment Routing over IPv6 Traffic Engineering
    3. SRv6 SRH：Segment Routing Header
    4. MPLS PE：Multiprotocol Label Switching Provider Edge
    5. SRv6 SID：Locator + Function Opcode
    6. MPLS CE：Multiprotocol Label Switching Customer Edge
    7. IS-IS：Intermediate System to Intermediate System
