# coding=utf-8
# @Author:ChenBo lin

"""
import sys

# print(sys.path)  # 打印环境变量
print(sys.argv)

"""

import os

# cmd_res = os.system('dir')  # 执行命令，不保存结果
cmd_res = os.popen('dir').read()
print('---->', cmd_res)

# 在当前目录下新建一个文件
os.makedirs('new_dir')
