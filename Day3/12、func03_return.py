# coding=utf-8
# @Author:ChenBo lin


# # 一、return 会中止函数运行
# def test1():
#     print("in the test1")
#     return 0
#     print("text end")
#
# test1()


# # 二、用变量去接受函数返回值
# def test1():
#     print("in the test1")
#     return 0
#
# x = test1()
# print(x)



def test1():
    print("in the test1")

def test2():
    print("in the test2")
    return 0

def test3():
    print("in the test3")
    return 1, "hello", ["alex", "lala"], {"name": "kobe"}

x = test1()
y = test2()
z = test3()

print(x)
print(y)
print(z)

