from pylab import *
import pandas as pd
import numpy as np

if __name__ == '__main__':
    s = pd.Series([i * 2 for i in range(1, 11)])
    print(s)
    print(type(s))
    # 使用pandas制作 8行5列 的表格，索引使用时间序列，列使用 ABCDE ，值在10以内随机选择
    dates = pd.date_range("20210414", periods=8)
    df = pd.DataFrame(np.random.randint(10, size=(8, 5)), index=dates, columns=list("ABCDE"))
    print(df)

    # pandas基本操作

    # Basic
    # 打印前3行
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~Basic~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~Select~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("A列的数据：")
    print(df["A"])
    print("前3行 方式2：")
    print(df[:3])
    print("对指定索引间的数据进行切片：")
    print(df["2021-04-14":"2021-04-17"])
    print("显示日期索引第0列的值：")
    print(df.loc[dates[0]])
    print("显示指定索引和指定列的值：")
    print(df.loc["2021-04-14":"2021-04-15", ["B", "D"]])
    print("取出指定索引和指定列的值：")
    print(df.at[dates[0], "C"])
    print("显示指定下标行，指定下标列的数据：")
    print(df.iloc[1:3, 2:4])
    print("取出指定下标行，指定下标列的数据。方式1：")
    print(df.iloc[1, 4])
    print("取出指定下标行，指定下标列的数据。方式2：")
    print(df.iat[1, 4])
    print("显示所有大于0的元素：")
    print(df[df > 0])
    print('''显示 "E" 列为 "2/4/8"的所有元素：''')
    print(df[df["E"].isin([2, 4, 8])])

    # Set
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~Set~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('''给原本的表格上追加一列 "F"，并填入值 ''')
    sl = pd.Series(list(range(10, 18)), index=pd.date_range("20210414", periods=8))
    df["F"] = sl
    print(df)
    print("修改第一行，A列的值为0：")
    df.at[dates[0], "A"] = 0
    print(df)
    print("修改第二行，第二列的值为1：")
    df.iat[1, 1] = 1
    print(df)
    print("修改 D 列所有的值：")
    df.loc[:, "D"] = np.array([4] * len(df))
    print(df)

    # 对缺失值的处理
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~对缺失值的处理~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("取出上述表格前4行的值，加一列空值 G，作为新的表格 ：")
    df1 = df.reindex(index=dates[:4], columns=list("ABCD") + ["G"])
    print(df1)
    print("给第一，二行的G列赋值为1")
    df1.loc[dates[0]:dates[1], "G"] = 1
    print(df1)
    print("不显示有 NaN 的数据行列")
    print(df1.dropna())
    print("填充所有为 NaN 的数据")
    print(df1.fillna(value=6))

    # 拼接
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~Concat~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("将df的前3行和后3行拼接到一起：")
    pieces = [df[:3], df[:-3]]
    cdf = pd.concat(pieces)
    print("拼接后的类型：", type(cdf))
    print("拼接后的数据：")
    print(cdf)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~merge~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # 新键两个DataFrame来做merge测试
    left = pd.DataFrame({"key": ["x", "y"], "value": [1, 2]})
    right = pd.DataFrame({"key": ["x", "z"], "value": [3, 4]})
    print("DataFrame1:", left)
    print("DataFrame2:", right)
    print("将两个DataFrame合并，选择的合并方式类似sql中的 left join：")
    print(pd.merge(left, right, on="key", how="left"))
    print("将两个DataFrame合并，选择的合并方式类似sql中的 inner join：")
    print(pd.merge(left, right, on="key", how="inner"))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~groupby~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # 新键一个DataFrame来做聚合测试
    gdf = pd.DataFrame({"A": ["a", "b", "c", "b"], "B": list(range(4))})
    print("聚合前:")
    print(gdf)
    print("聚合后:")
    print(gdf.groupby("A").sum())

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~时间序列~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # 10个时间段，以秒为单位累加
    date_exam = pd.date_range("20210415", periods=10, freq="S")
    print(date_exam)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~绘图~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ts = pd.Series(np.random.randn(1000), index=pd.date_range("20210415", periods=1000))
    ts = ts.cumsum()
    ts.plot
    show()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~读取文件~~~~~~~~~~~~~~~~~~~~~~~~~~")
    excel_df = pd.read_excel("../resources/XX月XX月的考勤表.xlsx")
    print(excel_df)
    print("保存到新的excel")
    excel_df.to_excel("../resources/test.xlsx")
