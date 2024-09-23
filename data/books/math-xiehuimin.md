# 《谢惠民数学分析习题集》读书笔记

## 1.1 关于习题课教案的组织

- `2024-09-23` 阅读 《谢惠民数学分析习题集》1.1

-  介绍了作者关于习题课组织以及教案编写的一些心得体会。
- 对老师：
  - 习题课教师必须自己动手解题并选题，不能随便从书上抄题。
  - 教师认真批改作业、思考其中出现的问题是上好习题课的必要条件。
  - 学生当堂可能提出新的解法，老师应当能现场判断出其正确与否，并分析其价值和意义。
- 对学生：
  - 不论习题课中习题的选择是怎样的如花似锦，学生还是必须经过自己的实践才能吸收其中所含的营养。
  - Polya：模仿 +  实践。

## 1.2 书中常用记号

- `2024-09-23` 阅读 《谢惠民数学分析习题集》1.2
- 未指明取值范围的数一律认为属于实数 $\bold R$。
- $O_{\delta}(a)=U_{\delta}(a)=(a-\delta, a+\delta)$ 表示开邻域，$\delta$ 在语义清晰的前提下可以省略。

## 1.3 几个常用的初等不等式

### 1.3.1  几个初等不等式的证明

- `2024-09-23` 阅读 《谢惠民数学分析习题集》1.3.1

#### 伯努利不等式

- 设 $h>-1, n\in N_+$，则成立不等式：

$$
(1+h)^n\geq 1+nh
$$

- 首先 $n=1$ 时，不等号两侧始终等于 $1+h$，因此不等式成立。
- 其次，当 $h=0$ 时，不等号两侧的值也始终等于 1,因此不等式成立。
- 于是我们只需要证明 $n\geq 2$ 且 $h\neq 0$ 的情况。
- 我们联想到等比数列求和公式：
  - 在 $q\neq 1, n\geq 1$ 时，$1+q+q^2+\cdots+q^{n-1}=\frac{q^n-1}{q-1}$
  -  由于 $h\neq 0$，因此 $1+h\neq 1$，所以可以带入 $q=1+h$ 得到
  - $h(1+(1+h)+(1+h)^2+\cdots+(1+h)^{n-1})=(1+h)^n-1$
- 于是只需要证明 $(1+h)^n-1\geq nh$
  - 即 $h(1+(1+h)+(1+h)^2+\cdots+(1+h)^{n-1})\geq nh$
  - 由于要考虑 $h$ 的正负号，所以我们不能鲁莽地把左右两侧约去 $h$
- 如果 $h>0$，我们只要证明
  - $1+(1+h)+\cdots+(1+h)^{n-1}\geq n$
  - 由于左侧总共有 $n$ 项，且其中每一项都大于等于一，所以不等式成立
- 如果 $h < 0$，我们需要证明
  - $1+(1+h)+\cdots+(1+h)^{n-1}\geq n$
  - 由于题目中有 $h>-1$ 的条件，因此此时 $0<1+h<1$
  - 因此左侧的 $n$ 项构成了单调递减的正项等比数列，因此其中每一项都小于等于一，所以不等式成立
- 我在中学时期证明过这个不等式，但是当时使用的是求导的方式。
  - 但是我觉得用求导的方式证明初等不等式并不是一个好习惯。一个严谨的数学体系应当避免把根基建立在一个我们还未严谨定义的东西之上。
  - 不过仅从正确性验证的角度而言，求导的方式未尝不可。

#### 伯努利不等式的双参数版本

- 设 $A>0, A+B>0, n\in N_{+}$，则成立不等式：

$$
(A+B)^n\geq A^n+nA^{n-1}B
$$

- 且当 $n>1$ 时，等号成立的充分必要条件是 $B=0$。
- 证明比较简单，由于 $A>0$ 因此可以两侧同时除以 $A^n$
  - $(1+\frac{B}{A})^n\geq 1+n\cdot \frac{B}{A}$
- 由于 $A+B>0$，因此 $1+\frac{B}{A}>0$ 即 $\frac{B}{A}>-1$
  - 将 $h=\frac{B}{A}$ 代入伯努利不等式即可

#### 算术几何均值不等式的基础形式

- 本文中提到了以下三种均值不等式

$$
a\geq 0, b\geq 0 \Rightarrow \sqrt{ab}\leq \frac{1}{2}(a+b)
$$

$$
ab>0 \Rightarrow \frac{b}{a}+\frac{a}{b}\geq 2
$$

$$
a^2+b^2\geq 2ab
$$

- 由于实数运算的性质，有 $(a-b)^2\geq 0$
  - 于是 $a^2-2ab+b^2\geq 0$ 即 $a^2+b^2\geq 2ab$
- 若 $ab>0$ 可以在基础形式两侧同时除以 $ab$
  - $\frac{a}{b}+\frac{b}{a}\geq 2$
- 若 $a\geq 0, b\geq 0$ 可以将 $a'=\sqrt a, b‘=\sqrt b$  代入基础形式。
  - $a+b\geq 2\sqrt{ab}$ 即 $\frac{1}{2}(a+b)\geq \sqrt{ab}$

#### 算术几何均值不等式的一般形式

$$
a_1\geq 0, a_2\geq 0, \cdots, a_n\geq 0 \Rightarrow \frac{a_1+a_2+\cdots+a_n}{n}\geq \sqrt[n]{a_1a_2\cdots a_n}
$$

- 等号成立的条件为 $a_1=a_2=\cdots=a_n$
- 书中给出了多种证明方式：
  - 使用伯努利不等式，借助一般数学归纳法求解。
  - 使用柯西**向前向后法**做反向数学归纳求解。
- 感觉柯西向前向后法确实十分精彩，简单写一下思路。
  - 设 $P(k)$ 表示 $k$ 个变量的均值不等式。
  - 首先证明 $k\geq 2 \Rightarrow(P(k)\Rightarrow P(2k))$，由于 $P(2)$ 成立，因此可以证明 $P(2^k)$ 均成立。
    - 这里就一直用二元均值不等式倍增即可。
  - 再证明 $k\geq 3\Rightarrow(P(k)\Rightarrow P(k-1))$ ，由于任意 $k$ 一定存在一个比它大的二的整数次幂，因此整体得证。
    - 这里我们需要在 $k-1$ 元均值不等式中补一个元素，使它成为一个 $k$ 元均值不等式。
    - 补的元素是这 $k-1$ 个数的算术平均值。 

#### 三角不等式（三点不等式）

$$
|a+b|\leq |a|+|b|
$$

- 反复使用 $-A\leq x\leq A \Leftrightarrow |x|\leq A$
- $-|a|\leq a\leq |a|$
- $-|b|\leq b\leq |b|$
- 得到 $-(|a|+|b|)\leq a+b\leq(|a|+|b|)$
- 得到 $|a+b|\leq |a|+|b|$

#### 柯西施瓦兹不等式

$$
\left|\sum_{i=1}^na_ib_i\right|\leq \sqrt{\sum_{i=1}^na_i^2}\cdot \sqrt{\sum_{i=1}^nb_i^2}
$$

- 前几天刚写过一个证明，不再写一次了。
  - 详见 [2024-09-17_corr.md](../../data/2024a-rand/2024-09-17_corr.md)
  - 需要注意的是，要将其中的期望写成均值的形式，其他地方变化不大。

## 正弦正切不等式

$$
0<x<\frac{\pi}{2} \Rightarrow \sin x\leq x\leq \tan x
$$

- 可以使用几何方法得到证明：即三角形和扇形的面积关系。

<img src="../../blob/img/2024-09-23_sin-x-tan.png">

- 取一个半径为 1 的圆，取圆心角弧度为 $x$，则
  - 三角形 $AOB$ 的面积为 $\frac{1}{2}\sin x$
  - 扇形 $AOB$ 的面积为 $\frac{1}{2} x$
  - 三角形 $AOC$ 的面积为 $\frac{1}{2} \tan x$
