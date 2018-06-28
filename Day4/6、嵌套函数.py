# coding=utf-8
# @Author:ChenBo lin

# def foo():
#     print("in the foo")
#     def bar():
#         print("in the bar")
#
#     bar()
# foo()



def grandfa():
    x = 100
    def father():
        x = 50
        def me():
            x = 25
            def son():
                x = 5
                print(x)
            son()
        me()
    father()
grandfa()
