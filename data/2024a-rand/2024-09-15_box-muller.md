# 《Box-Muller 方法正确性证明》`2024-09-15`

## 课上内容

- 老师上课似乎有这样的内容，我觉得不太对劲：
- 设 $R=\sqrt{x^2 + y^2},\theta=\tan^{-1}\frac y x$ 则当 $x, y$ 服从标准高斯分布的时，$R$ 和 $\theta$ 服从均匀分布。
- 我觉得不对劲啊，这个 $\theta$ 服从均匀分布我觉得直觉上还算勉强合理。
- 但这 $R$ 能取到正无穷吧，我们难道还能构造出一个零到正无穷的均匀分布来？这显然是不可能的。

## 一些证明

- 接下来我们先证明这个 $\theta$ 确实是均匀分布。
- 现在有 cdf 函数 $F_{x, y}(x, y)=\frac {1}{2\pi}e^{\frac{x^2+y^2}{2}}$
- 因此新 cdf $F_{R,\theta}(R, \theta)=F_{x, y}(R\cos \theta, R\sin \theta)\cdot |\mathcal J|$
- 其中

$$
\mathcal J=\left|\det\begin{pmatrix}
R_x & \theta_x\\
R_y & \theta_y
\end{pmatrix}\right|
$$

- 未完待续 ......

