# BMI = 体重/（ 身高 ** 2 ）
user_weight = float(input("请输入您的体重(单位为kg):"))
user_height = float(input("请输入您的身高(单位为m):"))
user_bmi = user_weight / (user_height ** 2)
user_gender = input("请输入您的性别（先生/女士）：")
print(user_gender + "，" + "您的BMI值为" + str(user_bmi))

if user_bmi <= 18.5:
    if user_gender == "女士":
        print("女士，您的体重属于偏瘦范围。")
    else:
        print("先生，您的体重属于偏瘦范围。")
elif 18.5 < user_bmi <= 25:
    if user_gender == "女士":
        print("女士，您的体重属于正常范围。")
    else:
        print("先生，您的体重属于正常范围。")
elif 25 < user_bmi <= 30:
    if user_gender == "女士":
        print("女士，您的体重属于偏胖范围。")
    else:
        print("先生，您的体重属于偏胖范围。")
else:
    if user_gender == "女士":
        print("女士，您的体重属于肥胖范围。")
    else:
        print("先生，您的体重属于肥胖范围。")
