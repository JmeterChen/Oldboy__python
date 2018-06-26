# coding=utf-8
# @Author:ChenBo lin

# key-value
"""
1、字典是无序的

"""

info = {
    'stu1101': 'TengLan Wu',
    'stu1102': 'LongZe Luola',
    'stu1103': 'XiaoZe Maliya'
}

"""

print(info)
# print(info['stu1101'])
info['stu1101'] = "武藤兰"
info['stu1104'] = 'CangJingKong'
print(info)


# del
del info['stu1101']
print(info)

# pop
info.pop('stu1101')
print(info)

# popitem 随机删  尽量少用
info.popitem()
print(info)
"""

# # 查找
# print(info.get('stu1103'))
#
# # 判断
# print('stu1104' in info)   # info.has_key('stu1103')   ----> in py2.x
#
#
# # 打印字典的值
# print(info.keys())
# # 打印字典的键
# print(info.values())
#
# # 将一对键-值加入字典中，如果键已经存在字典中，那么就不加进去，如果键不存在字典中，就会加进去
# info.setdefault('stu1104', 'yingjinliya')
# print(info)



# b = {
#     'stu1101': 'kobe',
#     1:3,
#     2:5
# }
# # 将b加入info字典中，当有相同键的时候，用b覆盖a的内容
# info.update(b)
# print(info)


# # 将字典中的键值对以元组的形式打印出来
# print(info.items())


# 初始化一个新字典
# c = dict.fromkeys([6, 7, 8], "test")
# print(c)

# # 类似浅copy
# c = dict.fromkeys([6, 7, 8], [8, {'name': 'kobe'}, 24])
# print(c)
# c[7][1]['name'] = 'james'
# print(c)

# 字典的循环  方法一比方法二高效的多
# 方法一
for i in info:
    print(i, info[i])

# 方法二
for k, v in info.items():
    print(k, v)