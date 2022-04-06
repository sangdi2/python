# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 15:49
# @Author : 张思惠
# @File : shoppingcart.py
# @Software : PyCharm
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffffee",31],["Book",60],["Nike",699]]
addproduct=[]
addindex=[]
print("-"*6+"商品购物列表"+"-"*6)

for i in range(len(products)):
    print(i,end="\t")
    for item in products[i]:

        print(item,end="\t")
    print(" ")
flag="f"
while flag!="q":
    str = input("请问您想买什么？请输入商品编号(按q退出购买)")
    if str.isdigit():
        if int(str)>=0 and int(str)<=5:
            addproduct.append(products[int(str)])
            addindex.append(int(str))
        else:
            print("您输入的商品编号无效")
            continue
    elif str=="q":
        break
    else:
        print("您的输入内容不符合规范")
        continue
print("-"*6+"商品购物列表"+"-"*6)

for j in range(len(addproduct)):
    print(addindex[j],end="\t")
    for name in addproduct[j]:
        print(name,end="\t")
    print(" ")
