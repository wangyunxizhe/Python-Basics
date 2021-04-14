import numpy as np
import matplotlib.pyplot as plt

# 使用matplotlib进行图表的绘制
if __name__ == '__main__':
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    # 构建图表中的线，并指定样式
    plt.plot(x, c, color='blue', linewidth=1.0, linestyle="-", label="COS", alpha=0.8)
    plt.plot(x, s, color='red', linewidth=1.0, linestyle=":", label="SIN")
    plt.title("TEST:COS SIN")
    # 获取轴编辑器
    ax = plt.gca()
    # 隐藏右边框
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    # 将Y轴设置到数据中间位置
    ax.spines["left"].set_position("zero")
    # 将X轴设置到数据中间位置
    ax.spines["bottom"].set_position("zero")
    # 将x轴的数据显示在x轴的下方
    ax.xaxis.set_ticks_position("bottom")
    # 将y轴的数据显示在y轴的左方
    ax.yaxis.set_ticks_position("left")

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        #更改x，y轴上的字体大小
        label.set_fontsize(16)
        #更改x，y轴上字体的背景
        label.set_bbox(dict(facecolor="red", edgecolor="None"))

    #图表数据线的图例，显示位置在左上方
    plt.legend(loc="upper left")
    #显示网格线
    plt.grid()
    plt.show()
