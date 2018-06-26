# coding=utf-8
# @Author:ChenBo lin

# age_of_oldboy = 56
# count = 0
# while count < 3:
#     guess_age = int(input('guess age: '))
#
#     if guess_age == age_of_oldboy:
#         print('yes,you got it!')
#         break
#     elif guess_age > age_of_oldboy:
#         print('think smaller!')
#     else:
#         print('think bigger!')
#     count += 1
#     if count == 3:
#         countine_confirm = input('do you want to keep guessing....?')
#         if countine_confirm != 'n':
#             count = 0
# # else:
# #     print('you have tried too many times...fuck off')

"""
for i in range(0, 10):
    if i < 3:
        print('loop', i)
    else:
        continue
    print('hehe')
"""

for i in range(10):
    print('-----------', i)
    for j in range(10):
        print(j)
        if j > 5:
            break