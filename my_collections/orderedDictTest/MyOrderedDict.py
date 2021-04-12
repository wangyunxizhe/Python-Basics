from collections import OrderedDict

# dict默认有序
user_dict = OrderedDict()
user_dict['b'] = "wy1"
user_dict['a'] = "wy2"
user_dict['c'] = "wy3"
print(user_dict)
# 将 key=b 的元素移动至最后
user_dict.move_to_end("b")
print(user_dict)
