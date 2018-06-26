# coding=utf-8
# @Author:ChenBo lin

"""
字符串操作：


"""

name = "my \tname is kobe bryant"
test = "a\tb"
print(len(test))
name1 = "my name is {name} and i am {age} old!"

print(name.capitalize())              # 首字母大写
print(name.count("a"))                # 统计字母个数
print(name.center(50, "-"))           # 一共50个字符,居中显示，不够的用的“-”代替
print(name.endswith("ant"))           # 判断字符串是否以某个字符串结尾
print(name.expandtabs(tabsize=30))    # 字符串中\t转换为一定长度的空格
print(name.find("name"))              # 查找指定字符的位置
print(name[name.find("name"):])       # 字符串切片
print(name1.format(name='kobe bryant', age=23))    # 占位符
print(name1.format_map({'name': 'kobe bryant', 'age': 23}))  # 类似上一个
print('abc123'.isalnum())             # 判断字符串 是否只包含26字母与数字
print('Asdfssf'.isalpha())            # 判断字符串 是否只包含26个字母（大小写均可）
print('1465'.isdigit())               # 判断字符串 是否都是数字
print('1A'.isidentifier())            # 判断字符串 是否是一个合法的标识符 （是否为一个合法的变量名）
print("是否全是小写:", 'a1we2fdf11'.islower())         # 判断字符串中字母是否全是小写
print("是否全是大写:", 'My Name Is Kobe'.isupper())    # 判断字符串中的字母是否全是大写
print('a 1aA'.isnumeric())
print('     '.isspace())              # 判断字符串是否全是空格
print('My Name Is Kobe'.istitle())    # 判断字符串中是否所有的单词第一个字母都是大写

print('-'.join(['1', '2', '3', '4']))
print(name.ljust(50, '*'))            # 将字符串从左边加入，长度变为50，不够的加*
print(name.rjust(50, '*'))            # 将字符串从右边加入，长度变为50，不够的加*
print(name.lower())
print(name.upper())

print('\nKobe\n'.lstrip())            # 去掉字符串左边的空格
print('\nKobe\n'.rstrip())            # 去掉字符串右边的空格
print('\nKobe\n'.strip())             # 去掉字符串左右两边的空格
print('-------')

# 简单加密的方法  注意做笔记
p = str.maketrans("abcdef", '123456')
p_ = str.maketrans("123456", 'abcdef')
m = ("kobe bryant".translate(p))
print(m)
n = (m.translate(p_))
print(n)

print('kobe bryant bsfdbs'.replace('b', 'B'))  # 替换字符串中的字符为其他的指定的字符
print('kobe bryant bsfdbs'.replace('b', 'B', 2))  # 替换字符串中的字符为其他的指定的字符,并且限定替换次数

print('kobe++—bryant'.rfind('b'))    # 查找字符串中靠右边的指定字符的位置

print('1+2+3+4'.split('+'))          # 字符串中在指定的字符使用分割
print('1+2\n+3+4'.splitlines())      # 字符串中在换行处进行分割

print('Kobe Bryant'.swapcase())      # 字符串中字母大写变小写，小写变大写

print(name.zfill(50))                # 将字符串长度补全为50，不够的用0填充
