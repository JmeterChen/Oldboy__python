# coding=utf-8
# @Author:ChenBo lin


# # **kwargs  把N个关键字参数，转换为字典的方式
# def test2(**kwargs):
#     print(kwargs)
#     print(kwargs['name'])
#     print(kwargs['age'])
#     print(kwargs['num'])
#
# test2(name="kobe", age=40, num=24)
#
# test2(**{'name': "james", "age": 33, "num": 23})



# # **kwargs与关键字参数一起使用
# def test3(name,  **kwargs):
#     print(name)
#     print(kwargs)
#
# test3('kobe', age=18, num=24)



# # **kwargs与默认参数一起使用
# def test4(name, age=18, **kwargs):
#     print(name)
#     print(age)
#     print(kwargs)
#
# # test4('kobe', num='24',team='Lakers')
# test4('kobe', num='24',team='Lakers',age=40)




# *args与**kwargs
def test5(name, age=18, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("NBA")

def logger(source):
    print("from %s" % source)

test5('kobe',age=40,num=24,team='Lakers')