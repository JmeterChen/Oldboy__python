# coding=utf-8
# @Author:ChenBo lin

# name = []
names = ['kobe', 'james', 'wade', 'paul', 'tatumu', 'wade']
# print(names)
# print(names[0])
# print(names[1:3])  # 切片
#
# print(names[-2:])   # 切片

# print(names[0:3])   # 切片
# print(names[:3])    # 切片


# names.append('chenbolin')   # 新增
# print(names)
#
# names.insert(1, 'yaoming')   # 在指定位置新增
# print(names)
#
# names[2] = 'james666'        # 更改
# print(names)


# # 删除
# names.remove('tatumu')
# print(names)

# # 删除元素
# del names[1]
# print(names)

# # 删除变量
# del names
# print(names)

# names.pop(1)
# print(names)

# # 查找
# print(names.index('paul'))
# print(names[names.index('paul')])


# # 统计元素个数
# print(names.count('wade'))

# # 清空列表
# names.clear()
# print(names)

# # 反转(倒序)
# print(names)
# names.reverse()
# print(names)

# # 排序 按照ASCII的顺序排列
#
# list_test = ['4nba', 'cba', 'chen', '#adsf', 'pikaqiu', 'Xiaozhu']
# list_test.sort()
#
# print(list_test)

# # 合并 注意与append的区别
# names2 = [1, 2, 3, 4]
# names.extend(names2)
# print(names)


# # 复制copy 浅copy
#
# names_old = ['kobe', 'james', 'wade', 'paul', ['nba', 'cba'], 'tatumu']
# # names_new = names_old.copy()
# names_new = names_old.copy()
# print(names_old, id(names_old))
# print(names_new, id(names_new))
#
# names_old[0] = '科比'
# names_old[4][0] = 'NBA'
# print(names_old, id(names_old[0]), id(names_old[4][0]))
# print(names_new, id(names_new[0]), id(names_new[4][0]))


# # 深copy
#
# import  copy
# names_old = ['kobe', 'james', 'wade', 'paul', ['nba', 'cba'], 'tatumu']
# names_new = copy.deepcopy(names_old)
# print(names_old, id(names_old))
# print(names_new, id(names_new))
#
# names_old[0] = '科比'
# names_old[4][0] = 'NBA'
# print(names_old, id(names_old[0]), id(names_old[4][0]))
# print(names_new, id(names_new[0]), id(names_new[4][0]))


# 列表循环
# for i in names:
#     print(i)

print(names[0:-1:2])
print(names[::2])
print(names[:])