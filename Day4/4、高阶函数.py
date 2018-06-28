# coding=utf-8
# @Author:ChenBo lin

import time

"""
高阶函数
        a：把一个函数名称当做实参传递给另一个函数
        (在不修改被装饰的函数源代码的情况下为其添加功能)
"""

def bar():
    time.sleep(3)
    print("in the bar")

def test1(func):
    star_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time is %s" % (stop_time-star_time))


# test1(bar)
bar()
