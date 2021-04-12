from collections import Counter

# 使用Counter统计元素出现的次数
users = ["wy1", "wy2", "wy3", "wy1", "wy2", "wy1"]
myCount = Counter(users)
print(myCount)
print(type(myCount))

# 统计重复字符出现次数
myCount = Counter("adasdasbcavchaj")
print(myCount)
# 使用update可以使Counter更灵活
myCount.update("bbbbbsssss")
print(myCount)
myCount2 = Counter("cccddd")
myCount.update(myCount2)
print(myCount)
# 还可以用来解决Top n的问题
print(myCount.most_common(1))#Top1
print(myCount.most_common(2))#Top2
