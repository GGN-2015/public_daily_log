# 《Box-Muller 方法正确性证明》`2024-09-15`

## 课上内容

- 老师上课似乎有这样的内容，我觉得不太对劲：
- 设 $R=\sqrt{x^2 + y^2},\theta=\tan^{-1}\frac y x$ 则当 $x, y$ 服从标准高斯分布的时，$R$ 和 $\theta$ 服从均匀分布。
- 我觉得不对劲啊，这个 $\theta$ 服从均匀分布我觉得直觉上还算勉强合理。
- 但这 $R$ 能取到正无穷吧，我们难道还能构造出一个零到正无穷的均匀分布来？**这显然是不可能的**。
- 我猜 $R$ 应该是一种奇奇怪怪的分布，与此同时 $\theta$ 是 $0\sim 2\pi$ 上的均匀分布。 

## 一些直觉

- **雅可比矩阵**的本质是微元换系的一阶近似。

$$
\begin{pmatrix}\text d u\\ \text d v\end{pmatrix}=
\begin{pmatrix}
	\frac{\partial u}{\partial x} & \frac{\partial u}{\partial y}\\
	\frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}\\
\end{pmatrix}
\begin{pmatrix}\text d x\\ \text d y\end{pmatrix}
$$

- **雅可比矩阵的行列式**的本质是微元换系时面积的增益倍数。

$$
\mathcal J=\begin{pmatrix}
	\frac{\partial u}{\partial x} & \frac{\partial u}{\partial y}\\
	\frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}\\
\end{pmatrix}
$$

- 则 $\det \mathcal J$ 的含义是，$\text d u\text d v$ 构成的面积是 $\text d x \text d y$ 构成的面积的多少倍。

## 证明一元概率换元

- 设 $Y=h(X)$，$X=g(Y)$，其中 $h(x)$ 单调递增或者递减。已知 $X\sim \text{p.d.f}\;F_X$ 求 $Y\sim \text{p.d.f}\;?$
- 不妨假设 $h(x)$ 单调递增。

$$
\int_{-\infty}^{y_0}F_Y(y)\text d y=P[Y\leq y_0]=\mathbb P[X \leq h^{-1}(y_0)]=\int_{-\infty}^{h^{-1}(y_0)}F_X(x)\text d x
$$

- $\text d x=g'(y) \text d y$
- 于是得到 $F_Y(y)=F_X(g(y))\left|g'(y)\right|$
- 这里的一个直觉是 $g(y)$ 的带入放缓了坐标前进的速度，导致最终面积超过 $1$，放缓的部分应当用系数 $g'(y)$ 补偿回来。
- 这里我们可以理解，里面填入了 $g(x)$，因此速度被放慢了 $\frac{1}{g'(x)}$ 倍，因此需要在外面补偿修正一个 $g'(x)$。

## 类比二元概率换元

- 已知 $X, Y\sim \text{p.d.f} \; F_{X,Y}$，$U=h_1(X, Y), V=h_2(X, Y)$，求 $U, V \sim \text{p.d.f} \; ?$
- 设 $X=g_1(U, V), Y=g_2(U, V)$
- 则 $F_{U, V}(u, v)=F_{X, Y}(g_1(U, V), g_2(U, V))\cdot |\mathcal J|$
- 其中 $\mathcal J = \frac{\partial(X, Y)}{\partial (U, V)}$，类似于一元概率换元，这里的 $|\mathcal J|$ 同样可以用来补偿面积增益。

## 关键证明

- 设 $\text{p.d.f}\;$ $F_{X, Y}(x, y)=\frac{1}{2\pi} e^{-\frac{x^2+y^2}{2}}$ 是二维标准高斯分布。
- $R=\sqrt{x^2+y^2}, \theta=\tan^{-1}\frac{y}{x}$ 求 $R, \theta$ 服从什么分布？最后能算出来：

$$
F_{R,\theta}=\frac{R}{2\pi}e^{-\frac{R^2}{2}}
$$

- 这说明 $\theta$ 服从定义域内的均匀分布，且 $R$ 和 $\theta$ 相互独立，其中 $\frac{1}{2\pi}$ 是 $\theta$ 的分布函数。
- 接下来我们需要找到一种用于生成 $R$ 的算法。

## 生成指定分布的随机变量

- 设 $\mathcal F(x)$ 是 $\text{c.d.f}$，可以证明 $X=\mathcal F^{-1}(U)\sim \text{c.d.f} \mathcal \; F$

$$
\mathbb P[X\leq x_0]=\mathbb P[\mathcal F^{-1}(U) \leq x_0]=\mathbb P[U\leq \mathcal F(x_0)]=\mathcal F(x_0)
$$



- 因此，考虑如何生成 $R$ 时，我们可以先使用 $\text{p.d.f}$ 不定积分计算出 $\text{c.d.f}$，然后再求它的反函数。

- 得到 $R$ 服从 $\text{c.d.f}$ $\mathcal F(r)=1-e^{-\frac{r^2}{2}}$
- 于是 $\mathcal F^{-1}(y)=\sqrt{-2\ln (1-y)}$
- 考虑到 $1-U$ 和 $U$ 实际上是同分布，因此可以使用 $r=\sqrt{-2\ln U}$ 来实现随机数的生成。

## Box-Muller 定理

- 设 $U_1$ 和 $U_2$ 是两个相互独立的标准均匀分布。
  - $R=\sqrt{-2\ln U_1}$
  - $\theta=2\pi U_2$
  - $X=R\cos \theta$
  - $Y=R\sin \theta$
  - 根据上文中的分析，可以证明 $X, Y$ 服从相互独立的标准高斯分布。

