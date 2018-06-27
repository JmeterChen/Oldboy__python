# coding=utf-8
# @Author:ChenBo lin


#  ！！！最好避免这样使用  作死行为


# def change_name():
#     global name
#     name = 'kobe'
#
#
# change_name()
# print(name)



names = ['kobe', 'wade', 'paul']

def change_name():

    names[0] = 'chenbolin'
    print(names)


change_name()
print(names)