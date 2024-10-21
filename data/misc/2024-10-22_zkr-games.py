dic = {}
sol = {}
mxd = {}
mxs = {}
SUM = 31

def f(a, b, c) -> float:
    return (15 + (a + b + c) + 3*a) * (1 + b/15) * (1 / (1 - c * 0.03)), 

for a in range(SUM + 1):
    for b in range(SUM + 1 - a):
        for c in range(min(SUM + 1 - a - b, 20 + 1)):
            d = a + b + c
            v = f(a, b, c)
            if c == 0:
                if dic.get(d) is None:
                    dic[d] = v
                    sol[d] = (a, b, c)
                else:
                    dic[d] = max(dic[d], v)
                    if dic[d] == v:
                        sol[d] = (a, b, c)
            if (c != 20 and a == 0 and b == 0) or c == 20:
                if mxd.get(d) is None:
                    mxd[d] = v
                    mxs[d] = (a, b, c)
                else:
                    mxd[d] = max(mxd[d], v)
                    if mxd[d] == v:
                        mxs[d] = (a, b, c)

import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 数据
x  = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
d4 = []
d5 = []

for i in range(SUM + 1):
    x.append(i)
    y1.append(sol[i][0])
    y2.append(sol[i][1])
    y3.append(sol[i][2])
    d4.append(dic[i])
    d5.append(mxd[i])
    y4.append(mxs[i][0])
    y5.append(mxs[i][1])
    y6.append(mxs[i][2])
    a, b, c = sol[i]
    print({
        "d": i, 
        "ans": d4[-1], 
        "a": a, 
        "b": b, 
        "c": c, 
        "sa": (15 + (a + b + c) + 3*a), 
        "sb": (1 + b/15), 
        "sc": (1 / (1 - c * 0.03))
    })

# 绘制三条折线
axs[0, 0].plot(x, y1, label='A', marker='o')
axs[0, 0].plot(x, y2, label='B', marker='s')
axs[0, 0].plot(x, y3, label='C', marker='^')

# 添加标题和标签
axs[0, 0].set_title('ABC')
axs[0, 0].set(xlabel='X-axis', ylabel='Y-axis')

# 添加图例
axs[0, 0].legend()


# 绘制三条折线
axs[0, 1].plot(x, y4, label='A', marker='o')
axs[0, 1].plot(x, y5, label='B', marker='s')
axs[0, 1].plot(x, y6, label='C', marker='^')
axs[0, 1].legend()


axs[1, 0].plot(x, d4, label='D1', marker='o')
axs[1, 0].plot(x, d5, label='D2', marker='s')
axs[1, 0].legend()

# 显示图形
plt.show()
