# coding=utf-8
# @Author:ChenBo lin

product_list = [('iphone', 5800),
                ('mac pro', 12800),
                ('starbark', 30),
                ('iwatch', 3000),
                ('bike', 800),
                ('python', 120)]

shopping_list = []
salary = input('请输入你的工资： ')
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("请选择你要购买的商品：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice> -1:
                item_p = product_list[user_choice]
                if salary >= item_p[1]:  # 买得起
                    salary -= item_p[1]
                    shopping_list.append(item_p)
                    print("Add %s into shopping car, your balance is \033[31;1m%s\033[0m" % (item_p, salary))
                else:                    # 买不起
                    print("\033[41;1m你的余额只剩[%s]啦，还买个锤子\033[0m" % salary)
            else:
                print("product code [%s] is not exist!" % user_choice)
        elif user_choice == 'q':
            print("---------shopping list ---------------")
            for p in shopping_list:
                print(p)
            print("Your current balance:", salary)
            exit()
        else:
            print("input is ERROR!!!")

else:
    print("请输入正确工资数目！！！")