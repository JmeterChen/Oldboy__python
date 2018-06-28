# coding=utf-8
# @Author:ChenBo lin

import time

def bar():
    time.sleep(3)
    print("in the bar")


def test2(func):
    print(func)
    return func


# print(test2(bar))

# t = test2(bar)
# t()

bar = test2(bar)
bar()  # run bar