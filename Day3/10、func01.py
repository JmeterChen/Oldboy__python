# coding=utf-8
# @Author:ChenBo lin

"""
1、面向对象       类----》class
2、面向过程       过程----》def
3、函数式编程      函数----》def
"""

# 函数
def func1():
    """testing"""
    print("in the func1")
    return 0

# 过程
def func2():
    """testing2"""
    print("in the func2")


x = func1()
y = func2()

print("from func1 return is %s" % x)
print("from func2 return is %s" % y)
