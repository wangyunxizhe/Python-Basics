import numpy as np

# numpy中的基础属性
if __name__ == '__main__':
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    # shape:获取np_lst的形状（2行3列）
    print(np_lst.shape)
    # ndim:数组的维度
    print(np_lst.ndim)
    # dtype:数组元素的数据类型
    print(np_lst.dtype)
    # size:np_lst中元素的总数
    print(np_lst.size)
    # 生成2行，4列元素都为0的二维数组
    zeros_list = np.zeros([2, 4])
    print(zeros_list)
    # 生成3行，5列元素都为1的二维数组
    ones_list = np.ones([3, 5])
    print(ones_list)

    print("Rand 2行4列:", np.random.rand(2, 4))
    print("Rand 单个:", np.random.rand())

    # 1-10中随机选3个数组成列表
    print("RandInt:", np.random.randint(1, 10, 3))

    print("Randn:", np.random.randn(2, 4))

    # 在给定的范围内随机选取1个数
    print("Choice:", np.random.choice([10, 20, 30]))

    print("Distribute:", np.random.beta(1, 10, 5))

    ####################常用操作####################
    # 构建含元素1-10的一维数组，再拆分成2行5列的二维数组
    npl = np.arange(1, 11).reshape([2, 5])
    print(npl)
    # 每个元素的平方
    print(np.exp2(npl))

    l1 = np.array([10, 20, 30, 40])
    l2 = np.array([4, 3, 2, 1])
    print(l1 + l2)
    print(l1 - l2)
    print(l1 / l2)
    print(l1 * l2)
    print(l1 ** l2)
    # 将2个nparray合并
    print(np.concatenate((l1, l2)))
    # 将2个nparray组成二维数组
    print(np.vstack((l1, l2)))
