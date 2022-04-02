# -*- codeing = utf-8 -*-
# @Time : 2022/4/2 13:00
# @Author : 张思惠
# @File : random.py
# @Software : PyCharm
import random
a = input("请输入：剪刀（0）、石头（1）、布(2):")
d =int(a)
b = random.randint(0,2)
c = ["剪刀","石头","布"]

print(c[b])
if b==d:
    print("你的输入为：%s(%d)" %(c[d],d))
    print("随机生成数字为：%d" %b)
    print("这局是平局")
elif d-b==1 or d-b==-2:
    print("你的输入为：%s(%d)" %(c[d],d))
    print("随机生成数字为：%d" %b)
    print("这局你赢了")
else:
    print("你的输入为：%s(%d)" %(c[d],d))
    print("随机生成数字为：%d" %b)
    print("这局你输了")



