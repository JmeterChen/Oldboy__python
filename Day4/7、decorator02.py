# coding=utf-8
# @Author:ChenBo lin

import time


"""
第一步改造

def deco(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time is %s" % (stop_time-start_time))

def test1():
    time.sleep(3)
    print("in the test1")

def test2():
    time.sleep(3)
    print("in the test2")

deco(test1)
deco(test2)

"""


"""
第二步改造

def deco(func):
    start_time = time.time()
    return func
    stop_time = time.time()
    print("the func run time is %s" % (stop_time-start_time))

def test1():
    time.sleep(3)
    print("in the test1")

def test2():
    time.sleep(3)
    print("in the test2")


test1 = deco(test1)
test1()
test2 = deco(test2)
test2()
"""

"""
第三步改造
def timmer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s" % (stop_time-start_time))
    return deco

def test1():
    time.sleep(3)
    print("in the test1")

def test2():
    time.sleep(3)
    print("in the test2")

test1 = timmer(test1)
test1()
test2 = timmer(test2)
test2()

"""


"""
终极改造
"""

def timmer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s" % (stop_time-start_time))
    return deco


@timmer  # 等价于test1 = timmer(test1)
def test1():
    time.sleep(3)
    print("in the test1")

@timmer
def test2():
    time.sleep(3)
    print("in the test2")




# test1 = timmer(test1)
# test1()
# test2 = timmer(test2)
# test2()

test1()
test2()
