# coding=utf-8
# @Author:ChenBo lin

# def test(x, y):
#     print(x)
#     print(y)
#
# test(1, 2)   # 与形参一一对应



# def test(x, y):
#     print(x)
#     print(y)
#
# x = 2
# y = 1
#
# test(y=y, x=x)


def test(x, y):
    print(x)
    print(y)

test(y=2, x=1)  # 关键字参数与形参顺序无关

"""
记住一点，关键字参数不能写在形式参数前面就可以
"""