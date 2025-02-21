# class nameofclass :
# 类用驼峰命名方法, __init__(self): 表示构造函数，表示实例对象的属性

# class CuteCat:
#     def __init__(self):
#         self.name = "lambton"
# 此步骤为定义对象的属性

# cat1 = CuteCat()
# print(cat1.name)
# 此步骤为创建对象cat1，对象的命名方式为类名（），括号内放入参数

# class CuteCat:
#     def __init__(self, cat_name):
#         self.name = cat_name
#
#
# cat1 = CuteCat("Jojo")
# print(cat1.name)

# class CuteCat:
#     def __init__(self, cat_name, cat_age, cat_color):
#         self.name = cat_name
#         self.age = cat_age
#         self.color = cat_color
#
#
# cat1 = CuteCat("lily", 2, "orange")
# print(f"小猫{cat1.name}的年龄是{cat1.age}，花色是{cat1.color}")
# print("喵" * self.age)

# class CuteCat:
#     def __init__(self, cat_name, cat_age, cat_color):
#         self.name = cat_name
#         self.age = cat_age
#         self.color = cat_color
#
#     def speak(self):
#         print(f"喵{self.age}")
#
#     def think(self,content):
#         print(f"小猫{self.name}正在思考{content}...")
#
#
# cat1 = CuteCat("lily", 1.5, "orange")
# cat1.think("今天吃点儿什么好呢")
# cat1.speak()

# 练习：定义一个学生类
# 要求：
# 1.属性包括学生姓名、学号、以及语数外三科成绩
# 2.能够设置某科科目
# 3.能够打印该学生所有成绩

# 我的答案：

# class Student:
#     def __init__(self, student_name, student_id, student_chinese, student_math, student_english):
#         self.name = student_name
#         self.id = student_id
#         self.chinese = student_chinese
#         self.math = student_math
#         self.english = student_english
#
#
# student1 = Student("Ming", 123456, 98, 95, 99)
# print(f"学生{student1.name}，学号：{student1.id},语文成绩为{student1.chinese}，数学成绩为{student1.math}，英语成绩为{student1.english}。")

# 参考答案：

# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.id = student_id
#         self.grades = {"语文": 0, "数学": 0, "英语": 0}
#
#     def set_grade(self, course, grade):
#         if course in self.grades:
#             self.grades[course] = grade
#
#     def print_grade(self):
#         print(f"学生{self.name}，学号{self.id}的成绩为：")
#         for course in self.grades:
#             print(f"{course}:{self.grades[course]}分")
#
#
# chen = Student("chen", 11001)
# lin = Student("lin", 11002)
# chen.set_grade("英语", 98)
# print(chen.grades)
# chen.set_grade("数学", 90)
# chen.set_grade("历史", 60)
# chen.print_grade()

# 类继承练习
# 1.员工分为两类：全职员工fulltimeemployee、兼职员工parttimeemployee
# 2.全职和兼职都有“姓名 name”，“工号 id”属性，都具备“打印信息 print_info”（打印姓名、工号）方法
# 3.全职有"monthly_salary"属性
#   兼职有daily_salary属性、“每月工作天数 work_days”的属性
# 4.全职和兼职都有“计算月薪calculate_monthly_pay的方法，但具体计算过程不一样

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def print_info(self):
        print(f"员工{self.name},工号为{self.employee_id}。")


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)
        self.monthly_salary = 0

    def calculate_monthly_pay(self):
        print(f"员工{self.name}的月薪为{self.monthly_salary}")


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)
        self.daily_salary = 0
        self.work_days = 0

    def calculate_monthly_pay(self):
        monthly_salary = self.daily_salary * self.work_days
        print(f"员工{self.name}的月薪为{monthly_salary}")


wang = FullTimeEmployee("小王", 11001)
wang.print_info()
wang.monthly_salary = 3000
wang.calculate_monthly_pay()
