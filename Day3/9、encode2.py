# encoding=gbk
# @Author:ChenBo lin

import sys
print(sys.getdefaultencoding())


s = '你哈'
print(s)

"""
1、不管你文件是用什么格式编写的，但是python默认的是unicode格式读取的
2、并且在编码的时候，会将文件内容编码成byte类型，解码后就会复原
"""