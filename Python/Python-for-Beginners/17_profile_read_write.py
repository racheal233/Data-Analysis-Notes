# 绝对路径：从根目录出发，Windows用\区隔每以层级，MACOS用/
# 相对路径：从某一特定层级出发，自身是.，往上依次是..||../..

# 打开文件 Open(路径，'r'/'w',encoding='utf-8')   注意，第二个参数不写的话就默认为r
# r表示读取文件，如果路径错误会报错；

# 读取文件的方法
# 1.read 返回全部内容的字符串
# 2.readline 返回一行文件内容的字符串
# 3.返回全部文件内容组成的列表

# 关闭文件
# 1.调用close方法
# 2.with open(路径) as f:
#   print(f.read())  表示执行完print后的操作后就关闭文件

# f = open("./data.txt", "r", encoding='utf-8')
# content = f.read()
# print(content)
# f.close()

# with open("./data.txt", "r", encoding='utf-8') as f:
#     content = f.read()
#     print(content)

# with open("./data.txt", "r", encoding='utf-8') as f:
#     print(f.readline())
#     print(f.readline())

# with open("./data.txt", "r", encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# w表示写入文件，如果路径错误，会按照路径新创建文件，如果已有文件，会把文件清空
# a表示附加模式，如果路径已有文件，不会清空，二是会新增内容
# 写入文件的方法 .write，多次写入的内容不会自动换行
# 写入模式和附加模式下，不支持读取方法，解决方法是打开文件时，模式选择r+

# 练习案例：
# 任务1：在一个新的名字为poem.txt的文件中，写入以下内容：
# 我欲乘风归去，
# 又恐琼楼玉宇，
# 高出不胜寒。

# 任务2:在上面的poem.txt文件结尾处，添加以下两句：
# 起舞弄清影，
# 何似在人间。

# with open("./poem.txt", "w", encoding = 'utf-8') as f:
#     f.write('我欲乘风归去,\n又恐琼楼玉宇,\n高处不胜寒。')
# with open("./poem.txt", "a", encoding = 'utf-8') as f:
#     f.write('\n起舞弄清影，\n何似在人间。')

