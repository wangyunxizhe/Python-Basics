import pandas as pd
import numpy as np

if __name__ == '__main__':
    s = pd.Series([i * 2 for i in range(1, 11)])
    print(s)
    print(type(s))
    # 使用pandas制作表格
    dates = pd.date_range("20210414", periods=8)
    df = pd.DataFrame(np.random.randint(10, size=(8, 5)), index=dates, columns=list("ABCDE"))
    print(df)

    # pandas基本操作

    # Basic
    # 打印前3行
    print("前3行：")
    print(df.head(3))
    # 打印后3行
    print("后3行：")
    print(df.tail(3))
    print("索引列：")
    print(df.index)
    print("数据列：")
    print(df.values)
    # 行列反转
    print("反转后：")
    print(df.T)
    # 将列倒序为：EDCBA
    print(df.sort_index(axis=1, ascending=False))
    print(df.describe())

    # Select
    print("A列的数据：")
    print(df["A"])
    print("前3行 方式2：")
    print(df[:3])
    print("对指定索引间的数据进行切片：")
    print(df["2021-04-14":"2021-04-17"])
