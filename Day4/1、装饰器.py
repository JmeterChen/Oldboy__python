# coding=utf-8
# @Author:ChenBo lin

def test1():
    pass
    logger()


def test2():
    pass
    logger()

def logger():
    print("logging")


test1()
test2()


"""
------》》》
1、装饰器
2、定义：本质是函数，（装饰其他函数）就是为其他函数添加附加功能
3、原则
    1、不能修改被装饰的函数源代码
    2、不能修改被装饰的函数的调用方式（对于被装饰的函数来说，装饰器相当于路人）
"""

