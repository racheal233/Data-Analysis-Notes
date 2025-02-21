# 数字不能用引号包裹，**乘方，*乘号，/除号

# 导入math库可以解锁更多运算，例如例子中sqrt就表示开方，具体包含的函数类别和调用方式可以参考python官方文档
import math
a = 1
b = 9
c = 20
print((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
print((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
