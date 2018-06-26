# coding=utf-8
# @Author:ChenBo lin

import sys

# # 使用with，就不需要使用close（）去关闭文件，因为他自带关闭
# with open("yesterday", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line)


# 使用with可以一次性打开多个文件
with open("yesterday", "r", encoding="utf-8") as f , \
     open("yesterday.bak", "r", encoding="utf-8") as f2:
    for line in f:
        print(line)