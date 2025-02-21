# python的执行模式：
# 1-当前模式的命令行模式，python解释器逐行运行；
# 2-交互模式：输完一行后立即执行并展示（即便是没有键入print的情况下），在终端输入python3 进入交互模式

# 注释规则：只管单行；多行注释快捷方法：选中整段同时按command/control 和 /
# 对字符串求长度
s = "Hello world!"
print(len(s))

# 通过索引获取单个字符，索引是从0开始数
print(s[0])
print(s[11])

# 布尔类型
b1 = True
b2 = False

# 空值类型
n = None

# type函数 求变量的的数据类型
print(type(s))
print(type(b1))
print(type(n))
print(type(1.5))
