# coding=utf-8
# @Author:ChenBo lin


"""
def test(x, y, z=2):
    print(x)
    print(y)
    print(z)

test(1, 2)
"""



# 当实参个数很多但不固定时，形参怎么写？？？

# #接受N个位置参数，转换为元组形式
# def test(*args):
#     print(args)
#
# test(11, 22, 33, 44, 55)
#
# test(*[111, 222, 333, 444, 555])
#
#
# def test1(x, *args):
#     print(x)
#     print(args)
#
# test1(1,2,3,4,5,6)



# 参数组与默认参数一起使用
def test2(x, y =18,*args):
    print(x)
    print(y)
    print(args)

test2(11,22,33,44,55)
