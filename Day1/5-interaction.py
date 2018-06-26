# coding=utf-8
# @Author:ChenBo lin

# username = input('username :')
# password = input('password :')
# print(username, password)

# 格式化输出
# # 例一
# name = input("name: ")
# age = int(input('age: '))
# job = input('job: ')
# salary = input('salary: ')
#
# info = '''
# -----info of %s-----
# Name:%s
# Age:%d
# Job:%s
# Salary:%s
# ''' % (name, name, age, job, salary)
#
# print(info)


# # 例二
# name = input("name: ")
# age = int(input('age: '))
# job = input('job: ')
# salary = input('salary: ')
#
# info2 = '''
# -----info of {_name}-----
# Name:{_name}
# Age:{_age}
# Job:{_job}
# Salary:{_salary}
# '''.format(_name=name,
#            _age=age,
#            _job=job,
#            _salary=salary)
#
# print(info2)

# 例三
name = input("name: ")
age = int(input('age: '))
job = input('job: ')
salary = input('salary: ')

info3 = '''
-----info of {0}-----
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name, name, age, job, salary)

print(info3)