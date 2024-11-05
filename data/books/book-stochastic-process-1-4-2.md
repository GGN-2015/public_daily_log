# 《随机过程理论阅读笔记：1.4.2 标准化随机变量》`2024-11-05`

## 标准化随机变量

$$
X^*=\frac{X-E[X]}{\sqrt{D[x]}}
$$

- 可以证明，标准化随机变量的期望总是 $0$，方差总是 $1$

$$
\begin{aligned}
E[X^*]
&=E\left[\frac{X-E[X]}{\sqrt{D[X]}}\right]\\
&=\frac{1}{\sqrt{D[X]}} \cdot E[X-E[X]]\\
&=\frac{1}{\sqrt{D[x]}}\cdot(E[X]-E[X])\\
&=0
\end{aligned}
$$

$$
\begin{aligned}
D[X^*]
&=E\left[(X^*)^2\right]-E^2[X^*]\\
&=E[(X^*)^2]\\
&=E\left[\frac{(X-E[X])^2}{D[x]}\right]\\
&=\frac{1}{D[X]}\cdot E[(X-E[X])^2]\\
&=1
\end{aligned}
$$

## 例 1.4-1 求二项分布的期望和方差

- 设 $X\sim B(n, p)$，即 $P[X=k]=\binom{n}{k}\cdot p^k(1-p)^{n-k}$

### 二项分布的期望

$$
\begin{aligned}
E[X]
&=\sum_{i=0}^n i\cdot P[X=i]\\
&=\sum_{i=0}^n i\cdot \binom{n}{i}\cdot p^i\cdot (1-p)^{n-i}\\
&=\sum_{i=1}^n i\cdot \binom{n}{i}\cdot p^i\cdot (1-p)^{n-i}\\
&=(1-p)^n\cdot \sum_{i=1}^ni\cdot \binom{n}{i}\cdot \left(\frac{p}{1-p}\right)^i
\end{aligned}
$$

- 教材上的证明风格我不喜欢，教材上用到了阶乘展开，虽然我觉得差别不大吧，但是我还是喜欢求导的书写方式。设

$$
f(x)=\sum_{i=0}^n\binom{n}{i}\cdot x^{i}=(1+x)^n
$$

- 则有

$$
f'(x)=\sum_{i=1}^ni\cdot \binom{n}{i}\cdot x^{i-1}
$$

- 继续拼凑

$$
\begin{aligned}
g(x)=xf'(x)
&=\sum_{i=1}^n i\cdot \binom{n}{i}\cdot x^{i}\\
&=nx\cdot (1+x)^{n-1}
\end{aligned}
$$

- 现在我们回到 $E[X]$ 的表达式

$$
\begin{aligned}
E[X]
&=(1-p)^n\cdot \sum_{i=1}^ni\cdot \binom{n}{i}\cdot \left(\frac{p}{1-p}\right)^i\\
&=(1-p)^n\cdot g\left(\frac{p}{1-p}\right)\\
&=(1-p)^n\cdot n\cdot \frac{p}{1-p} \cdot\left(1 + \frac{p}{1-p}\right)^{n-1}\\
&=np
\end{aligned}
$$

### 二项分布的方差

- 因为我们已经计算得到了 $E[X]$ 的值，想要求方差，我们还需要知道 $E[X^2]$

$$
\begin{aligned}
E[X^2]
&=\sum_{i=0}^n i^2\cdot P[X=i]\\
&=\sum_{i=0}^n i^2\cdot \binom{n}{i}\cdot p^i\cdot (1-p)^{n-i}\\
&=\sum_{i=1}^n i^2\cdot \binom{n}{i}\cdot p^i\cdot (1-p)^{n-i}\\
&=(1-p)^n\cdot \sum_{i=1}^ni^2\cdot \binom{n}{i}\cdot \left(\frac{p}{1-p}\right)^i
\end{aligned}
$$

- 沿用上文中 $f(x)$ 和 $g(x)$ 的定义继续计算，设

$$
\begin{aligned}
h(x)=xg'(x)
&=\sum_{i=1}^n i^2\cdot \binom{n}{i}\cdot x^{i}\\
&=x\cdot\left(n(1+x)^{n-1}+n(n-1)x(1+x)^{n-2}\right)
\end{aligned}
$$

- 观察 $E[X^2]$

$$
\begin{aligned}
E[X^2]
&=(1-p)^n\cdot \sum_{i=1}^ni^2\cdot \binom{n}{i}\cdot \left(\frac{p}{1-p}\right)^i\\
&=(1-p)^n\cdot h\left(\frac{p}{1-p}\right)\\
&=(1-p)^n\cdot \left(\frac{p}{1-p}\right)\cdot\left(n\left(1+\left(\frac{p}{1-p}\right)\right)^{n-1}+n(n-1)\left(\frac{p}{1-p}\right)\left(1+\left(\frac{p}{1-p}\right)\right)^{n-2}\right)\\
&=(1-p)^n\cdot \left(\frac{p}{1-p}\right)\cdot\left(n(1-p)^{1-n}+n(n-1)\left(\frac{p}{1-p}\right)(1-p)^{2-n}\right)\\
&=np+n(n-1)p^2\\
&=np+n^2p^2-np^2
\end{aligned}
$$

- 于是

$$
\begin{aligned}
D[X]
&=E[X^2]-X^2[X]\\
&=(np+n^2p^2-np^2)-(np)^2\\
&=np-np^2\\
&=np(1-p)
\end{aligned}
$$

## 例 1.4-2 求泊松分布的期望和方差

- 设 $X\sim Po(\lambda)$ 即

$$
P[X=k]=\frac{e^{-\lambda}\cdot\lambda ^k}{k!}
$$

### 求泊松分布的期望

$$
\begin{aligned}
E[X]
&=\sum_{i=0}^\infty i \cdot P[X=i]\\
&=\sum_{i=0}^\infty i\cdot \frac{e^{-\lambda}\cdot\lambda ^i}{i!}\\
&=e^{-\lambda}\cdot \sum_{i=1}^\infty i\cdot \frac{\lambda^i}{i!}
\end{aligned}
$$

- 感觉还是可以用求导的思路解决问题，设 $f(x)=e^x$

$$
\begin{aligned}
f(x)=\sum_{i=0}^\infty\frac{x^i}{i!}
\end{aligned}
$$

- 于是

$$
\begin{aligned}
g(x)=xf'(x)
&=\sum_{i=1}^\infty i\cdot \frac{x^i}{i!}\\
&=x\cdot e^x
\end{aligned}
$$

- 回到 $E[X]$ 的定义

$$
\begin{aligned}
E[X]
&=e^{-\lambda}\cdot \sum_{i=1}^\infty i\cdot \frac{\lambda^i}{i!}\\
&=e^{-\lambda}\cdot g(\lambda)\\
&=e^{-\lambda}\cdot \lambda \cdot e^\lambda\\
&=\lambda
\end{aligned}
$$

### 求泊松分布的方差

- 由于已经知道了期望，因此只需要计算 $E[X^2]$

$$
\begin{aligned}
E[X^2]
&=\sum_{i=0}^\infty i^2 \cdot P[X=i]\\
&=\sum_{i=0}^\infty i^2 \cdot \frac{e^{-\lambda}\cdot\lambda ^i}{i!}\\
&=e^{-\lambda}\cdot \sum_{i=1}^\infty i^2\cdot \frac{\lambda^i}{i!}
\end{aligned}
$$

- 设 $h(x)=xg'(x)$

$$
\begin{aligned}
h(x)=xg'(x)
&=\left(x+x^2\right)\cdot e^x\\
&=\sum_{i=1}^\infty i^2\cdot \frac{x^i}{i!}
\end{aligned}
$$

- 回看 $E[X^2]$

$$
\begin{aligned}
E[X^2]
&=e^{-\lambda}\cdot \sum_{i=1}^\infty i^2\cdot \frac{\lambda^i}{i!}\\
&=e^{-\lambda}\cdot h(\lambda)\\
&=e^{-\lambda}\cdot \left(\lambda+\lambda^2\right)\cdot e^{\lambda}\\
&=\lambda+\lambda^2
\end{aligned}
$$

- 因此可以得到方差

$$
\begin{aligned}
D[X]
&=E[X^2]-E^2[X]\\
&=\lambda+\lambda^2-\lambda^2\\
&=\lambda
\end{aligned}
$$

