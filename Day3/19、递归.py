# coding=utf-8
# @Author:ChenBo lin

# 在函数内部，可以调用其他函数。如果在一个函数内部调用自身本身，这个函数就是递归函数

"""
递归特性：
1、必须有一个明确的结束条件
2、每次进入更深一层递归时，问题规模相比上一次递归都应有所减少
3、递归效率不高，递归层次过多会导致栈溢出
"""


# # 特性一   必须有一个明确的结束条件
# def calc(n):
#     print(n)
#     return calc(n+1)
#
# calc(0)


def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc(int(n/2))
    print("->", n)

calc(10)