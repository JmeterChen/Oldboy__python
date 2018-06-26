# coding=utf-8
# @Author:ChenBo lin

# 只有两个方法
# 一个是count、一个是index

# names = ('kobe', 'james')


# 作业
"""
需求：
    1、启动程序后，让用户输入工资，然后打印商品列表
    2、允许用户根据商品编号购买上商品
    3、用户选择商品后，检测余额是否足够，否就直接扣款，不够就提醒
    4、可随时退出，退出时打印购买商品和余额
"""


# 自己写的
salary = int(input("请输入你的工资： "))
list_shopping = [(0, 'iphone', 5800),
                 (1, 'macbook', 12800),
                 (2, 'stabuck Latte', 50),
                 (3, 'bike', 800),
                 (4, 'iwatch', 3000),
                 (5,'computer', 6500)]

list_shopping_num = []
list_shopping_thing = []
list_shopping_maney = []
for i in list_shopping:
    list_shopping_num.append(i[0])
    list_shopping_thing.append(i[1])
    list_shopping_maney.append(i[2])


shoping_car = []
while True:
    print("请选择商品1",list_shopping)
    shoping_x = input("请输入对应的商品编号：")
    if shoping_x == 'q':
        break
    elif int(shoping_x) in list_shopping_num and list_shopping_maney[int(shoping_x)] < salary:
        salary -= list_shopping_maney[int(shoping_x)]
        shoping_car.append(list_shopping_thing[int(shoping_x)])
    else:
        break

print(shoping_car, salary)