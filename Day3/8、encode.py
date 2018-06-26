# coding=utf-8
# @Author:ChenBo lin

s = "你哈"
print(s)


s_utf8 = s.encode("utf-8")
print(s_utf8)

s_gbk = s.encode("gbk")
print(s_gbk)

s_gbk_utf8 = s_gbk.decode("gbk").encode("utf-8")
print(s_gbk_utf8)


