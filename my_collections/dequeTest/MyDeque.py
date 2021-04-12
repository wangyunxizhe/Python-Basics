from collections import deque

# 将任何可以迭代的对象转化为 deque 类型（双端队列），并提供类似数组的实例方法
# 与list的区别：deque线程安全，而list不是
my_deque = deque(("wy1", "wy2", "wy3", "wy4"))
print(my_deque)
print(isinstance(my_deque, tuple))
print(type(my_deque, tuple))

# dict的keys是可以迭代的对象
my_deque = deque({"a": "wy1", "b": "wy2", "c": "wy3", "d": "wy4"})
print(my_deque)

my_deque = deque(["wy1", "wy2", "wy3", "wy4"])
my_deque.insert(2, "wy5")
print(my_deque)

# 反转
my_deque.reverse()
print(my_deque)
