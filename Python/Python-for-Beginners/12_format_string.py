# format方法："字符串{}".format(xx,xx)；
# {}里面如果是数字就表示，字符串在format中的位置，如果是其他字符串吗，则需要在format方法中对字符串进行赋值
# f-字符串：格式为f"字符串{}..."，效果是字符串中{}内的内容会被直接求值.

gpa_dict = {"Eric": 3.6, "alice": 3.78, "alex": 3.24, "john": 3.9}

# for name, gpa in gpa_dict.items():
#     print(name + '您好，您当前的绩点为：' + str(gpa))

for name, gpa in gpa_dict.items():
    print("{0}您好，你当前的绩点为：{1}".format(name, gpa))

# .items()，是一个字典方法，用来返回字典中每个键值对的元组形式，格式是 (key, value)。
