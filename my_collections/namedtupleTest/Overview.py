from collections import *

name_list = ['wy1', 'wy2']
for name in name_list:
    print(name)

name_tuple = ("wy", 1, 120, "nj")
# python的拆包：可以用多个参数去接元组中对应下标的值
n1, a1, h1, add = name_tuple
print(n1, a1, h1, add)
# 只单独取出元组里的第一个元素，其余元素装进新的列表中
n2, *arg = name_tuple
print(n2, arg)

# namedtuple：模拟创建 对象+属性，在创建简单对象时，可以代替class对象的传统方式（场景：在从数据库取数据做数据处理时，可以使用这样的方式，方便映射）
# 方式1
User = namedtuple("User", ["name", "age", "height"])
user = User(name="wy", age=1, height=11)
print(user.name)

# 方式2
User1 = namedtuple("User", ["name", "age", "height"])
user_tuple = ("wy", 1, 11)
use1 = User1(*user_tuple)
print(use1.name)

# 方式3
User2 = namedtuple("User", ["name", "age", "height", "edu"])
user_tuple2 = ("wy", 1, 11)
# 单独加上部分属性
use2 = User2(*user_tuple2, "master")
print(use2.name, use2.edu)

# 方式4：使用dict填充对象属性
User3 = namedtuple("User", ["name", "age", "height", "edu"])
user_dict = {"name": "wy", "age": 3, "height": 11}
# dict类型需要 ** 号
user3 = User3(**user_dict, edu="master")
print(user3.height, user3.edu)
