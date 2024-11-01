# 《骨肿瘤规划问题形式化》`2024-11-01`

- 设 $x^+_i$ 是所有正采样点所在的位置，即肿瘤组织所在的位置
- 设 $x^-_i$ 是所有负采样点所在的位置，即所有正常骨骼组织所在的位置
- 设 $a_jx+b_j\geq 0$ 是一组半空间，这些半空间的交集构成一个凸集
- 我们希望利用这个凸集去 “圈出” 所有的肿瘤组织
- 在此条件下，我们希望凸集内的正常骨的总量尽可能小

$$
\begin{aligned}
\min_{a, b}\;\;&\sum_{i}\min_{j}\{\varphi(a_jx^-_i+b_j)\}\\
\text{s.t.}\;\;&\forall i, j\;\;a_jx^+_i+b_j\geq 0\\
\text{where}\;\;&\varphi(x)=\left\{\begin{aligned}1, x\geq 0\\0, x<0\end{aligned}\right.
\end{aligned}
$$



- 只有下凸的东西才能求 min, 但目标函数一定不是下凸的
- 我断言这个东西没有什么太好的优化策略

## 一种可能可行的思路

- 考虑对 $\varphi(x)$ 进行连续化，以方便求导

$$
\varphi_k(x)=\frac{1}{1+e^{-kx}}
$$

- 其中 $k>0$ 是一个可以调节的参数
- 当 $k$ 越大，$\varphi_k(x)$ 越接近 $\varphi(x)$

