# 循环结构1 for in
# range函数 range（50）表示的是0到49，range（1，50）表示从1到49，还可以加上第三个数字，表示步长，没有标注步长的情况，默认为1；
# 循环结构2 while 条件A: （空行）行动B
#
# shopping_list =['socks','scarf','boots']

# for goods in shopping_list:
#    print(goods)

# for i in range(len(shopping_list)):
#     if i < len(shopping_list):
#         print(shopping_list[i])

# i=0
# while i < len(shopping_list):
#     print(shopping_list[i])
#     i=i+1

# 用while循环写一个对用户输入的数字求平均数的计算器
# ⚠️ 不用直接用float（）做判断条件，否则输入q会直接报错

# user_input = input("请依次输入数字，输入完成后以q结束，计算器会为您求取平均值：")
# total = 0
# count = 0
# while user_input != 'q':
#     num = float(user_input)
#     total += num
#     count += 1
#     user_input = input("请依次输入数字，输入完成后以q结束，计算器会为您求取平均值：")
# if count == 0:
#     print('您输入所有数字的平均值为0')
# else:
#     print("您输入所有数字的平均值为：" + str(total / count))