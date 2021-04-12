from collections import defaultdict

# 创建默认的dict，value为int类型
default_dict = defaultdict(int)

users = ["wy1", "wy2", "wy3", "wy1", "wy2", "wy1"]
for user in users:
    # 传统方式，需要判空
    # if user not in default_dict:
    #     default_dict[user] = 1
    # else:
    #     default_dict[user] += 1

    # 使用defaultdict函数的方式，代码更加简单，性能也更好
    default_dict[user] += 1

print(default_dict)


# 创建默认的dict，value也为dict类型
def gen():
    return {"name": "wy", "age": 3}


default_dict2 = defaultdict(gen)
print(default_dict2["group1"])
print(default_dict2["group2"])
print(default_dict2)
