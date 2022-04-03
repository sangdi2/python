# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 15:12
# @Author : 张思惠
# @File : SensitiveWord.py
# @Software : PyCharm
flag = "y"
sensitive=["苍井空","暴力男"]
while flag=="y":
    str =input("请输入内容：")
    for item in sensitive:

        if str.find(item)!=-1:

            str=str.replace(item,"***")

    print(str)
    flag=input("您想继续吗？请输入y继续,输入n结束")