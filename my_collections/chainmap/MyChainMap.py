from collections import ChainMap

dict1 = {"a": "wy1", "b": "wy2"}
dict2 = {"b": "wy2", "c": "wy3"}
for k, v in dict1.items():
    print(k, v)
# 将dict1，2都合并起来，并去重
newDict = ChainMap(dict1, dict2)
# 注意：ChainMap并不是返回一个新的集合，而是指向已有的数据，方便像操作一个dict那样操作
# 所以当更改 key=a的value时，dict1中的数据也被更改了
print(newDict.maps)
newDict.maps[0]["a"] = "wy"
print(dict1)
for k, v in newDict.items():
    print(k, v)
