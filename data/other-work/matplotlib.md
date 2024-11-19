# 《图像相关工具的常见用法》

## matplotlib 三维图像绘制

```python
import numpy as np
import matplotlib.pyplot as plt

# 创建一个 3D 图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ============================== 绘制过程（略）============================== #

# 设置坐标轴范围，且要求坐标轴比例相等
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.set_box_aspect([1, 1, 1])  # 使 x, y, z 轴等长

# 显示图形
plt.show()
```

### 绘制一个有解析式的三维曲面

```python
# ============================== 获取 ax（略）============================== #

# 绘制一个有解析式的三维曲面
# 不用 slice 其实效率挺低的，仅用于解释工作原理
def my_plot_surface(ax, xbegin, xend, xnum, ybegin, yend, ynum, function, color):
    xpos = np.linspace(xbegin, xend, xnum)
    ypos = np.linspace(ybegin, yend, ynum)
    xx = np.zeros((xnum, ynum))
    yy = np.zeros((xnum, ynum))
    zz = np.zeros((xnum, ynum))
    for xindex in range(xnum):
        for yindex in range(ynum):
            xx[xindex, yindex] = xpos[xindex]
            yy[xindex, yindex] = ypos[yindex]
            zz[xindex, yindex] = function(xpos[xindex], ypos[yindex])
    ax.plot_surface(xx, yy, zz, alpha=0.5, color=color)

# 绘制一个三维空间中的正弦曲线
my_plot_surface(ax, -3, 3, 20, -3, 3, 20, lambda x, y: np.sin(x + y), 'cyan')

# ============================== 限制坐标范围，显示 plt（略）============================== #
```

### 绘制球体

```python
# ============================== 获取 ax（略）============================== #

# 绘制球体
def my_draw_ball(ax, centerx, centery, centerz, radius, rnum, color, alpha):
    u = np.linspace(0, 2 * np.pi, rnum)
    v = np.linspace(0, np.pi, rnum)
    x = centerx + radius * np.outer(np.cos(u), np.sin(v))
    y = centery + radius * np.outer(np.sin(u), np.sin(v))
    z = centerz + radius * np.outer(np.ones(np.size(u)), np.cos(v))
    print(x.shape, y.shape, z.shape)
    ax.plot_surface(x, y, z, color=color, alpha=alpha)

my_draw_ball(ax, 1, 2, -1, 1, 100, 'blue', 0.6)

# ============================== 限制坐标范围，显示 plt（略）============================== #
```

### 绘制任意曲面

```python
# ============================== 获取 ax（略）============================== #

# 假设有一个参数方程曲面
# 原始参数为 (u, v)，目标空间是三维空间 (x, y, z)
# 给出 function2to3 即可完成绘制
def my_plot_any_surface(ax, ubegin, uend, unum, vbegin, vend, vnum, function2to3, color, alpha):
    upos = np.linspace(ubegin, uend, unum)
    vpos = np.linspace(vbegin, vend, vnum)
    xx = np.zeros((unum, vnum))
    yy = np.zeros((unum, vnum))
    zz = np.zeros((unum, vnum))
    for uindex in range(unum):
        for vindex in range(vnum):
            u = upos[uindex]
            v = vpos[vindex]
            x, y, z = function2to3(u, v)
            xx[uindex, vindex] = x
            yy[uindex, vindex] = y
            zz[uindex, vindex] = z
    ax.plot_surface(xx, yy, zz, alpha=alpha, color=color)

# 绘制一个三维空间中的正弦曲线
def sample2to3(u, v):
    x = np.sin(u + v)
    y = u
    z = v
    return x, y, z

my_plot_any_surface(ax, -3, 3, 60, -3, 3, 60, sample2to3, 'cyan', 0.5)

# ============================== 限制坐标范围，显示 plt（略）============================== #
```

## vtk 三维图像绘制

### vtk 绘制 CT DICOM 数据

- 参考：`neko://Archive/2024-11-12_DogCT整理`

### vtk 绘制三维 numpy 数组数据

- 参考：`neko://Archive/2024-11-19_如何把vtk当三维画板`

