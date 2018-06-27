# coding=utf-8
# @Author:ChenBo lin

# team = 'NBA'
#
# def change_name(name):
#     team = 'Lakers'
#     print("before change", name, team)
#     name = "KOBE"  # 这个函数就是这个变量的作用域  这个变量只在函数调用时才可以使用
#     age = 23
#     print("after change", name)
#
#
# name = 'kobe'
# change_name(name)
# print(name)
# print(team)


"""
那怎么在函数内部中更改全局变量呢？？？
可以在函数中，申明要更改的变量为全局变量（使用global），这样在函数内部更改
该变量后，该变量在全局范围内也就被更改了
"""

team = 'NBA'

def change_name(name):
    global team
    team = 'CBA'
    print("before change", name, team)
    name = "KOBE"
    age = 23
    print("after change", name)


name = 'kobe'
change_name(name)
print(name)
print(team)

