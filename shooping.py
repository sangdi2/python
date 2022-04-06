# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 15:34
# @Author : 张思惠
# @File : shooping.py
# @Software : PyCharm
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffffee",31],["Book",60],["Nike",699]]
print("-"*6+"商品购物列表"+"-"*6)

for i in range(len(products)):
    print(i,end="\t")
    for item in products[i]:

        print(item,end="\t")
    print(" ")