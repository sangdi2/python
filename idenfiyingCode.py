# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 12:47
# @Author : 张思惠
# @File : idenfiyingCode.py
# @Software : PyCharm
import random
def idenfiyingcode():
    list = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]

    num = random.sample(list, 5)
    strr = ""
    value = strr.join(num)

    return value
inp="f"
result=idenfiyingcode()
print(result)
while inp!="q":


    inp =input("请输入验证码:（按q退出）")
    if inp==result:
        print("您输入的验证码正确")
        break
    elif inp=="q":
        print("您已成功退出")

    else:
        print("您输入的验证码错误")


