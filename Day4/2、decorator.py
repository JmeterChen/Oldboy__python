# coding=utf-8
# @Author:ChenBo lin

import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s" % (stop_time-start_time))
    return warpper

@timmer
def test1():
    time.sleep(3)
    print("in the test1")

test1()


"""
实现装饰器知识储备：
    1、函数即“变量”
    2、高阶函数
        a：把一个函数名称当做实参传递给另一个函数
        (在不修改被装饰的函数源代码的情况下为其添加功能)
        b：返回值中包含函数名
        (不修改函数的调用方式)
    3、嵌套函数
    
      
====》》》高阶函数+嵌套函数=》装饰器
"""