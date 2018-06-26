# coding=utf-8
# @Author:ChenBo lin


# 读写操作   用的比较多
f = open("yesterday2", "r+", encoding="utf-8")  # 文件句柄
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("---------------diao-------------")

print(f.readline())


# # 写读操作  没什么卵用
# f = open("yesterday2", "w+", encoding="utf-8")  # 文件句柄
# f.write("-------------diao------------------1\n")
# f.write("-------------diao------------------2\n")
# f.write("-------------diao------------------3\n")
# f.write("-------------diao------------------4\n")
# print(f.tell())
# f.seek(10)
# print(f.tell())
# f.readline()
# f.write("should be at the begining of the second line")

# # 追加读
# f = open("yesterday2", "a+", encoding="utf-8")  # 文件句柄


# # 二进制读
# f = open("yesterday2", "rb")  # 文件句柄
# print(f.readline())
# print(f.readline())
# print(f.readline())

# # 二进制写
# f = open("yesterday2", "wb")  # 文件句柄
# f.write("hello binary\n".encode())
# f.close()



