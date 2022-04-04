# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 14:13
# @Author : 张思惠
# @File : login.py
# @Software : PyCharm
import datetime
data=[]
str="f"
def time():
    now =datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
try:
    f = open("guest_book.txt", "a")
    while str!="q":
        str=input("请输入用户名:(按q退出)")
        if str=="q":
            break
        print("您好,%s"%str)

        data.append(str+"\t"+time()+"\n")

    for item in data:
        f.write(item)
    f.close()
except Exception as result:
    print(result)

