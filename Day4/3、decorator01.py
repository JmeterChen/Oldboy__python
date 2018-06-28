# coding=utf-8
# @Author:ChenBo lin

# def foo():
#     print("in the foo")
#     bar()
#
# foo()


# # 情况一
# def bar():
#     print("in the bar")
#
#
# def foo():
#     print("in the foo")
#     bar()
#
# foo()



# #情况二
# def foo():
#     print("in the foo")
#     bar()
#
# def bar():
#     print("in the bar")
#
# foo()


#情况三   函数即变量
def foo():
    print("in the foo")
    bar()

foo()

def bar():
    print("in the bar")

