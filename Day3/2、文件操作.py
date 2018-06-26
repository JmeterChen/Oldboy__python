# coding=utf-8
# @Author:ChenBo lin

"""
对文件操作
    1、打开文件，得到文件句柄并复制给一个变量
    2、通过句柄文件进行操作
    3、关闭文件
"""



# # 打开文件(读操作)
# # data = open("yesterday", encoding="utf-8").read()
# f = open("yesterday", encoding="utf-8") # 获取文件句柄
# data = f.read()
# data2 = f.read()
# print(data)
# print('--------------data2-------------------', data2)
#
#
# # 修改文件(写操作,新建一个)
# f = open("yesterday2", "w", encoding="utf-8")  # 获取文件句柄
#
# f.write("我爱北京，\n")
# f.write("天安门上太阳升")
#
#
# # a append 追加(写操作，追加在原内容后面)
# f = open("yesterday2", "a", encoding="utf-8")  # 获取文件句柄
#
# f.write("\n when i was young i listen to the radio \n")
# # data = f.read()
# # print("--rade", data)
# f.close()


# """
# 读取文件前5行
# """
# f = open("yesterday", "r", encoding="utf-8")  # 获取文件句柄
#
# # # 方法1
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
#
# # # 方法2
# # for i in range(5):
# #     print(f.readline())


# #low loop
# """
# 循环文件，第10行的时候不打印
# """
#
# f = open("yesterday", "r", encoding="utf-8")  # 获取文件句柄
# for index, line in enumerate(f.readlines()):
#
#     if index == 9:
#         print("-----我是分割线-----------")
#     else:
#         print(line.strip())


# # high loop
# count = 0
# f = open("yesterday", "r", encoding="utf-8")  # 获取文件句柄
# for line in f:
#     if count == 9:
#         print("-----我是分割线-----------")
#         count += 1
#         continue
#     print(line)



# # 显示光标位置   tell()
# f = open("yesterday", "r", encoding="utf-8")  # 获取文件句柄
# print(f.tell())
# print(f.read(5))
# print(f.tell())

# # 把光标移动到指定位置   seek()
# f = open("yesterday", "r", encoding="utf-8")  # 获取文件句柄
# print(f.tell())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.seek(72)
# print(f.readline())


# f = open("yesterday2", "r", encoding="utf-8")  # 获取文件句柄
# # print(f.encoding)
# f.write("hello1 \n")
# f.write("hello2 \n")
# f.write("hello3 \n")
# print(f.flush())


# 截断
f = open("yesterday2", "a", encoding="utf-8")  # 获取文件句柄

f.truncate(10)
