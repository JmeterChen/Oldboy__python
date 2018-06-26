# coding=utf-8
# @Author:ChenBo lin

"""
集合是一个无序的，不重复的数据组合，他的主要作用如下：
    一、去重 ，把一个列表变成集合，就自动去重了

    二、关系测试，测试两组数据之间的交集、差集、并集等关系

注意：集合也是无序的
"""

list_1 = set([1, 3, 5, 7, 9, 5, 7])
print(list_1, type(list_1))


list_2 = set([2, 3, 88, 66, 9])
print(list_1, list_2)

list_3 = {3, 5}
list_4 = {6, 8}

# 交集  .intersection()   运算符： &
print(list_1.intersection(list_2))
print(list_1 & list_2)

# 并集   运算符： |
print(list_1.union(list_2))
print(list_1 | list_2)

# 差集（我有你没有）
print(list_1.difference(list_2))
print(list_1 - list_2)
print(list_2.difference(list_1))


# 子集(包含关系)
print(list_1.issubset(list_2))


# 父集(包含关系)
print(list_1.issuperset(list_3))

# 反向差集
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)

print("---------------------")


# 无交集返回True
print(list_3.isdisjoint(list_4))



# 基本操作
list_1.add(999)   # 添加一项
print(list_1)


list_2.update([11, 22, 33])  # 添加多项
print(list_2)


# remove() 可以删除一项
list_1.remove(3)
print(list_1)


print(list_1.pop())  # 注意：因为集合中的元素是无序的，所以删除是任意的 需要对比列表中的pop方法

# print(list_1.remove('aaa'))
list_1.discard('aaa')