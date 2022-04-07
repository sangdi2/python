# -*- codeing = utf-8 -*-
# @Time : 2022/4/7 10:09
# @Author : 张思惠
# @File : test.py
# @Software : PyCharm
import random
list1 = []
for i in range(65,91):
 list1.append(chr(i))
for m in range(97,123):
 list1.append(chr(m))
for n in range(48,58):
    list1.append(chr(n))
    p = random.sample(list1,4)
    r = "".join(p)
    print("输出验证码：",r)

    while True:
     ma = r
     user =input("请输入验证码：")
     if ma == user:
       print("验证成功")
       break
    else:
       print("验证码错误请,重新输入验证码：")
