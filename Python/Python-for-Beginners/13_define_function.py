# 写一个计算BMI的函数,注意def函数中print的值并未保存，只做展示用，需保存的值，应return,否则函数返回空值

def bmi_function(weight, height):
    bmi_result = weight / height ** 2
    if bmi_result <= 18.5:
        category = "偏瘦"
    elif bmi_result <= 25:
        category = "正常"
    elif bmi_result <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"您的BMI类型为：{category}")
    return bmi_result


bmi_value = bmi_function(45, 1.53)
print(bmi_value)
