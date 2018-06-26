# coding=utf-8
# @Author:ChenBo lin

import getpass
_username = 'kobe'
_password = '123456'
# 将用户输入的内容赋值给name变量
user = input('请输入用户名：')
pwd = input('请输入密码: ')

if user == _username and pwd == _password:
    print('welcome user %s login' % user)
else:
    print('Wrong username or password!')

