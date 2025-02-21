# 逻辑优先级 not > and > or
shopping_list = []
shopping_list.append('围巾')
shopping_list.append('手套')
shopping_list.append('秋裤')
shopping_list.append('帽子')
shopping_list.remove('秋裤')
# []表示列表，列表list是可变类型变量，上面.append是“方法”，会直接改变原列表里的内容。而字符串、整数等为不可变变量，不能使用“方法”，应该使用函数，且函数不改变原变量的值，如需改变，需重新赋值。

# print(shopping_list)
# print(shopping_list[0])
# print(len(shopping_list))

price = [59, 39, 45]
max_price = max(price)
sort_price = sorted(price)
print(max_price)
print(sort_price)
