# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 13:36
# @Author : 张思惠
# @File : RWfile.py
# @Software : PyCharm
def writee():
    f = open("gushi.txt", "w")
    f.write("\t\t行宫\n\t元稹 〔唐代〕\n寥落古行宫，宫花寂寞红。\n白头宫女在，闲坐说玄宗。")
    f.close()
def copyy():
    f=open("gushi.txt","r")
    readreult=f.readlines()

    f = open("copy.txt", "w")
    for item in readreult:
        f.write(item)
    print("复制完成")
writee()
copyy()