# coding=utf-8
# @Author:ChenBo lin

# # pycharm中getpass不好使用，去cmd中执行py文件
import getpass

_username = 'kobe'
_password = '123456'

username = input('username: ')
password = getpass.getpass('password: ')


# print(username, password)

if _username == username and _password == password:
    print('Welcome user {name} login...'.format(name=username))
else:
    print('Invalid username or password!')
